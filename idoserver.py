from flask import Flask
app = Flask(__name__)

@app.route('/', methods=['POST'])
def ido():
    print("POST request")
    return 'Hello, World!'
