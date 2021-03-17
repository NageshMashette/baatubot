from flask import Flask, jsonify
from bot import chatbot_response
app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify({"about":"Homepage!"})

def decrypt(msg):
    string = msg
    new_string = string.replace("+", "")
    return new_string

@app.route('/home/<name>')
def hello_name (name):
    dec_msg = decrypt(name)
    response = chatbot_response(dec_msg)
    return response

if __name__ == '__main__':
    app.run()
