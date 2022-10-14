""" this is bot for whatsapp """
import json
import requests
from flask import Flask, request
from crypt import methods

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
