"""telegram for the bot"""

import requests
import json

from crypt import methods

from flask import Flask, request

app = Flask(__name__)

TOKEN = "your token"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)

 



