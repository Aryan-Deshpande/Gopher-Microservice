from flask import Flask
from dotenv import load_dotenv
 # create flask app
app = Flask(__name__)

    # load dotenv
load_dotenv()

    # import routes
from src import routes



