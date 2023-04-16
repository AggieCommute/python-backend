from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/', methods=['POST'])
def print_request():
    print(request.get_data())
    return 'OK'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=os.getenv('PORT'))