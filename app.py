import json
from flask import Flask, render_template, request, jsonify
import openai
from openai.error import RateLimitError
import os

app = Flask(__name__)
openai.api_key = os.getenv('OPENAI_API_KEY')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gtp4', methods=['GET', 'POST'])
def gpt4():
    if request.method == 'GET':
        user_input = request.args.get('user_input')
    else:
        messages = [{"role": "user", "content": user_input}]
    
    try:
        response = openai.ChatCompletion.create(
            model='gpt-4',
            messages=messages
        )
    except RateLimitError:
        content = "The server is experiencing a high volume of requests. Please try again later."

    return jsonify(content=content)

if __name__ == "__main__":
    app.run(debug=True)
