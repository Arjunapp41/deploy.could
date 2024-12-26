# app.py
from flask import Flask
import os
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!this service deployed using github action '

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('pdrt'8080')))
