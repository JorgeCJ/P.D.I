from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import json

key = 'AIzaSyDAbF2NbF94YRuV8lXwgCnP0bzav8nJZUE'
genai.configure(api_key=key)

app = Flask(__name__)
CORS(app)

def load_dataset():
    with open('dataset.json', 'r') as file:
        dataset = json.load(file)
    return dataset

def generate_refactor(input_code):
    dataset = load_dataset()

    prompt = f"Refatore o seguinte código para melhorar desempenho e clareza:\n{input_code}\nRefatoração com base nas boas práticas de Clean Code: {dataset['clean_code_best_practices']}\nSeja bem sucinto, com poucas explicações:"

    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(prompt)

    refactored_code = response.text
    return refactored_code

@app.route('/refactor', methods=['POST'])
def refactor():
    data = request.json
    input_code = data.get('input_code', '')
    
    if not input_code:
        return jsonify({'error': 'No code provided'}), 400
    
    refactored_code = generate_refactor(input_code)
    
    return jsonify({'refactored_code': refactored_code})

if __name__ == '__main__':
    app.run(port=5000)
