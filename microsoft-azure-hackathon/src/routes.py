from src import app
from flask import render_template, request, make_response, redirect, url_for
from dotenv import load_dotenv
import os

# create a get route
@app.route('/')
def yours():
    return render_template('index.html')


