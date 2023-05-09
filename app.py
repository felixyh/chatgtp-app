import json
from flask import Flask, render_template, request, jsonify
import openai
from openai.error import RateLimitError
import os

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gpt35', methods=['GET', 'POST'])
def gpt35():
    if request.method == 'GET':
        user_input = request.args.get('user_input')
    else:
        user_input = request.form['user_input']

    # user_input = request.args.get('user_input') if request.method == 'GET' else request.form['user_input']
    messages = [{"role": "user", "content": user_input}]
    try:
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=messages
        )
        content = response.choices[0].message["content"]
    except RateLimitError:
        content = "The server is experiencing a high volume of requests. Please try again later."

    return jsonify(content=content)

if __name__ == "__main__":
    app.run(debug=True)
    
