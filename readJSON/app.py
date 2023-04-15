from flask import Flask, jsonify
import requests, json
app = Flask(__name__)

def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str

@app.route('/readJSON', methods = ['GET'])
def GetJSON():
    try:
        response = requests.get('http://127.0.0.1:7000/getJSON')
        msg = json.loads(response.content)
        data = {
            "message" : reverse(msg['message'])
        }
    except requests.exceptions.ConnectionError as errh:
        data = {
            "message" : "ERROR"
        }
    return jsonify(data)
    
if __name__ == "__main__":
    app.run(debug=True, port=9000)