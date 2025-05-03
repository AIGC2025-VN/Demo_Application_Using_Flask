# demo_app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World! This is my very first Flask app!"

if __name__ == '__main__':
    app.run(debug=True)