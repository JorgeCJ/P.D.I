# REFATORADOR DE CÓDIGO

Esta é uma aplicação destinada a refatoração de códigos segundo o Clean Code através da utilização de inteligência artificial. 

## Detalhes do projeto

Para rodar esse projeto, primeiramente, digite no terminal do VsCode `pip install -r requirements.txt`. Após isso, digite `python main.py` no diretório da raiz do projeto para colocar o servidor em execução. Depois, entre no diretório `frontend/index.html`, aperte ` Crtl + Shift + p` e selecione a opção `Live Server`(caso não possua, pesquisar por extensão).

Em `prompt.md`, podemos ver alguns modelos interessantes de prompts. De forma geral, obterá uma resposta mais precisa seguindo esses modelos.

## Teste de código a ser refatorado
```javascript
const numbers = [1, 2, 3, 4, 5];

for (let i = 0; i < numbers.length; i++) {
    console.log(numbers[i]);
}
```
Ao simplesmente enviarmos este código e pedirmos para refatorar, com pouca precisão, sem utilizarmos um dos prompts exemplos e sem utilizar o dataset, obtivemos um output muito extenso. Agora, utilizando um dos prompts já montados, recebemos uma resposta muito mais precisa:

```javascript
const numbers = [1, 2, 3, 4, 5];

numbers.forEach(number => console.log(number));
```

## Código completo do backend comentado

```python
# Importando as bibliotecas necessárias
from flask import Flask, request, jsonify  # Flask para criação de API web
from flask_cors import CORS  # CORS para habilitar requisições de diferentes origens
import google.generativeai as genai  # Biblioteca para interagir com o Google Gemini
import json # Biblioteca para trabalhar com dados no formato JSON

# Chave de API do Google Gemini
key = 'AIzaSyDAbF2NbF94YRuV8lXwgCnP0bzav8nJZUE'
genai.configure(api_key=key)  # Configura a chave de API para autenticação com o modelo Gemini

# Criação da instância do Flask
app = Flask(__name__)

# Ativando CORS para permitir chamadas de APIs de diferentes origens
CORS(app)

# Função responsável por carregar o dataset, que servirá para a base de treinamento da I.A.
def load_dataset():
    with open('dataset.json', 'r') as file:
        dataset = json.load(file)
    return dataset

def generate_refactor(input_code):
    """
    Essa função é responsável por refatorar o código.
    input_code: O código de entrada que será refatorado.
    """
    # Carrega o Dataset
    dataset = load_dataset()

    # Criando o prompt para enviar ao modelo, explicando o que deve ser feito
    prompt = f"Refatore o seguinte código para melhorar desempenho e clareza:\n{input_code}\nRefatoração com base nas boas práticas de Clean Code: {dataset['clean_code_best_practices']}\nSeja bem sucinto, com poucas explicações:"

    # Definindo o modelo generativo para refatoração do código
    model = genai.GenerativeModel('gemini-1.5-flash')  # Especifica o modelo de IA para usar
    response = model.generate_content(prompt)  # Envia o prompt e obtém a resposta

    # O código refatorado vem como texto na resposta do modelo
    refactored_code = response.text
    
    # Retorna o código refatorado
    return refactored_code

@app.route('/refactor', methods=['POST'])
def refactor():
    """
    Endpoint que recebe o código para refatoração e retorna o código refatorado.
    """
    
    # Obtém os dados enviados na requisição JSON
    data = request.json
    
    # Extrai o código de entrada. Se não houver código, retorna um erro
    input_code = data.get('input_code', '')  # Pega o valor do código a ser refatorado
    
    # Se não receber código no corpo da requisição, retorna um erro 400
    if not input_code:
        return jsonify({'error': 'No code provided'}), 400
    
    # Chama a função para gerar a refatoração do código usando Google Gemini
    refactored_code = generate_refactor(input_code)
    
    # Retorna a resposta em formato JSON com o código refatorado
    return jsonify({'refactored_code': refactored_code})

# Verifica se o arquivo está sendo executado diretamente e inicia o servidor Flask
if __name__ == '__main__':
    app.run(port=5000)  # Inicia o servidor Flask na porta 5000
```