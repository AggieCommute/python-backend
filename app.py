from flask import Flask, request, jsonify
from flask_cors import CORS
from dateutil.parser import *
from datetime import datetime
import os

from typing import Dict

app = Flask(__name__)
CORS(app, support_credentials=True)

def process_request(data: Dict) -> Dict:
    source: str = data['source']
    destination: str = data['destination']
    timeless_date: datetime = parse(data['date'])
    dateless_time: datetime = datetime.strptime(data['time'], '%I:%M %p')
    time: datetime = datetime(
        year= timeless_date.year,
        month= timeless_date.month,
        day= timeless_date.day,
        hour= dateless_time.hour,
        minute= dateless_time.minute,
        second= dateless_time.second,
        microsecond= dateless_time.microsecond,
    )

    print("")
    print(f"Source: {source}")
    print(f"Destination: {destination}")
    print(f"Time: {time}")
    print("")

    response: Dict = {}

    return response

@app.route('/', methods=['POST'])
def receive_request():
    payload = request.get_json()
    # inputs = CommuteInputs(request)    
    if all(key in payload for key in ('source', 'destination')):
        return process_request(payload), 201
    else:
        response = {message: "Bad request. Please verify that both 'source' and 'destination' keys are provided with string values in the form of a JSON object."}
        return response, 400

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=os.getenv('PORT'))
    # app.run(host="127.0.0.1", port=5000)