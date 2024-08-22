import json
import numpy as np
from tensorflow import keras
from sklearn.preprocessing import LabelEncoder
import pickle
import streamlit as st

# Load the intents file
with open("intent.json") as file:
    data = json.load(file)

# Load trained model
model = keras.models.load_model('chat_model.h5')

# Load tokenizer object
with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

# Load label encoder object
with open('label_encoder.pickle', 'rb') as enc:
    lbl_encoder = pickle.load(enc)

# Parameters
max_len = 20

# Streamlit application
st.title("ChatBot Application")

def get_response(user_input):
    result = model.predict(keras.preprocessing.sequence.pad_sequences(tokenizer.texts_to_sequences([user_input]),
                                             truncating='post', maxlen=max_len))
    tag = lbl_encoder.inverse_transform([np.argmax(result)])
    
    for i in data['intents']:
        if i['tag'] == tag:
            return np.random.choice(i['responses'])

# User input
user_input = st.text_input("You: ", "Hello, how can you help me?")

if user_input:
    response = get_response(user_input)
    st.write("ChatBot: ", response)

st.write("Type 'quit' to end the chat.")
