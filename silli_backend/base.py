from flask import Flask
from flask_cors import CORS
from flask import render_template
from flask import request
import random
import json
import requests
from helpers import CurrentUser
from pprint import pprint

current_user = CurrentUser(first_name='Erick', last_name='Rubi', email='erub03@gmail.com', username='erub03')

api = Flask(__name__)
CORS(api)

@api.route('/profile')
def my_profile():
    # response_body = {
    #     "name": "Nagato",
    #     "about" :"Hello! I'm a full stack developer that loves python and javascript",
    #     "crossorigin":"true"
    # }
    
    return render_template(
        'index.html',
        user=current_user
    )

    # return response_body

