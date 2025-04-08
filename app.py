from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'This is flask-app-ecs'

@app.route('/health')
def health():
    return 'Server is up and running'