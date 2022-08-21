from flask import Flask
from flask import jsonify, redirect, url_for

from flask_cors import CORS

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    return jsonify({'status':'ok'}), 200

if __name__ == "__main__":
    app.run()

