from flask import Flask, request, jsonify
from helper import remove_punctuations,tokelnize_and_padding,generate_output
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def index():
    return str("Hello, This is MentBOT api.")

@app.route('/process_text', methods=['POST'])
def process_text():
    # Getting Input
    input_text = request.json.get('text', '')
    
    # Preprocessing
    input_text = remove_punctuations(input_text)
    input_text_tokenized = tokelnize_and_padding(input_text)

    # Getting Bot Reply
    op = generate_output(input_text_tokenized)

    return jsonify({'output_text': op})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)


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