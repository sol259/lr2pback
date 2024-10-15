import os
from flask import Flask, request, render_template, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
port = int(os.environ.get("PORT", 8000))
@app.route('/get-ip', methods=['GET'])

def get_ip():
    #user_ip = request.remote_addr
    user_ip = request.access_route[0] #127.0.0.1 fix
    #return render_template('index.html', user_ip=user_ip)
    return jsonify({"ip": user_ip})


if __name__ == '__main__':
    app.run()
