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





'''
What is mental health?
What does it mean to have a mental illness?
Who does mental illness affect?
What causes mental health problems?
What are some of the warning signs of mental illness?
Can you prevent mental health problems?
Can people with mental illness recover?
What should I do if I know someone who appears to have the symptoms of a mental disorder?
How can I find a mental health professional for myself or my child?
What treatment options are available?
If I become involved in treatment, what do I need to know?
What is the difference between mental health professionals?
How can I find a mental health professional right for my child or myself?
Where else can I get help?
If I feel better after taking medication, does this mean I am "cured" and can stop taking it?
Where can I go to find therapy
Where can I learn about types of mental health treatment?
What are the different types of mental health professionals?
Where can I go to find a support group?
Where can I go to find inpatient care?
'''