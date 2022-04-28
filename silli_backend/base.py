from flask import Flask, Response, request
from flask_cors import CORS
from flask import render_template
import random
import json
import requests
from helpers import CurrentUser
from pprint import pprint
from transformers import AutoTokenizer, AutoModelForCausalLM


current_user = CurrentUser(first_name='Erick', last_name='Rubi', email='erub03@gmail.com', username='erub03')

api = Flask(__name__)
CORS(api)

@api.route('/index')
def my_profile():
    # response_body = {
    #     "name": "Nagato",
    #     "about" :"Hello! I'm a full stack developer that loves python and javascript",
    #     "crossorigin":"true"
    # }
    
    return render_template(
        'startpage.html',
        user=current_user
    )

    # return response_body


@api.route('/sentence', methods=['GET', 'POST'])
def get_sentence():
    word = ""
    if request.method == "POST":
        try:
            word = request.form['inputword']
        except:
            errors.append(
                "Unable to get URL. Please make sure it's valid and try again."
            )
            return render_template('index.html', errors=errors)
    if word:
        print(word)

        tokenizer = AutoTokenizer.from_pretrained("gpt2")
        model = AutoModelForCausalLM.from_pretrained("gpt2")

        prompt = " Sorry I'm late today because I saw a "+word + " and "
        input_ids = tokenizer(prompt, return_tensors="pt").input_ids

        # generate up to 30 tokens
        outputs = model.generate(input_ids, do_sample=False, max_length=30)
        sentence = tokenizer.batch_decode(outputs, skip_special_tokens=True)

        return render_template(
            'index.html',
            user=current_user,
            sentence=sentence
        )


@api.route('/home')
def my_home():
    sentence = "Sorry I'm late today because I saw a "
    return render_template(
        'index.html',
        user=current_user,
        sentence=sentence
    )

