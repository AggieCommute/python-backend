from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def print_request():
    print(request.json)
    return 'OK'

if __name__ == '__main__':
    app.run()