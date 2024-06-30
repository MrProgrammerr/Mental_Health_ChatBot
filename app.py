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
