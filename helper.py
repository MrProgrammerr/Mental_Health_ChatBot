import pickle
import string
import joblib
import random
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model

input_shape = 19
le = joblib.load('label_encoder.pkl')
responses = joblib.load('responses.pkl')
with open('tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)
model = load_model("my_bot.h5")
def remove_punctuations(text):
    ltrs = [ltrs.lower() for ltrs in text if ltrs not in string.punctuation]
    pure_text = "".join(ltrs)
    return pure_text

def tokelnize_and_padding(text):
    tokenized = tokenizer.texts_to_sequences([text])
    tokenized = np.array(tokenized).reshape(-1)
    padded = pad_sequences([tokenized],input_shape)
    return padded
def generate_output(padded):
    output = model.predict(padded,verbose=False)
    output = np.argmax(output)
    response_tag = le.inverse_transform([output])[0]
    res = random.choice(responses[response_tag])
    return res
