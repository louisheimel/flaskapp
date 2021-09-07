from flask import Flask
from flask import request
import time
import requests
app = Flask(__name__)

def get_timestamp():
    return str(time.time()).replace('.', '')

@app.route('/uploadpdf', methods = ['POST'])
def user():
    if request.method == 'POST':
        print(request.files['file'])
        auth = request.authorization
        username = auth['username']
        uploaded_file = request.files['file']
        # TODO: check if user is authorized
        if uploaded_file.filename != '':
            uploaded_file.save("folder/" + get_timestamp() + "_" + username + "_" + uploaded_file.filename)
        return "hello"
