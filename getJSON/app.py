from flask import Flask, jsonify, request, render_template, url_for
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/getJSON', methods = ['GET'])
def GetJSON():
   if (request.method =='GET'):
       data = {
           "id" :  1,
           "message" : "Hello Message"
       }
       return jsonify(data)
        

if __name__ == "__main__":
    app.run(debug=True,port=7000)