from flask import Flask, Response, request
from flask_cors import CORS
from flask import render_template
import random
import json
import requests
from helpers import CurrentUser
from pprint import pprint
from transformers import AutoTokenizer, AutoModelForCausalLM, GPT2Tokenizer, GPT2LMHeadModel



current_user = CurrentUser(first_name='Erick', last_name='Rubi', email='erub03@gmail.com', username='erub03')

api = Flask(__name__)
CORS(api)

lines=[]
with open('../language_models/sentence-prompts.txt') as f:
    lines = f.readlines()
line_num=0
pieces = lines[line_num].split("_")
paragraph=""
prevsentence=""
showSpinner = False

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

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


'''@api.route('/sentence1', methods=['GET', 'POST'])
def get_sentence1():
    global line_num
    global paragraph
    pieces = lines[line_num].split("_")
    fullsentence = ""
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
        fullsentence=pieces[0]+word #+pieces[1]
        # fullsentence = paragraph+pieces[0]+word+pieces[1]
        print(word)
        # link = 'distilgpt2'
        # link = 'dummy'
        # link = 'EleutherAI/gpt-j-6B'
        

        tokenizer = AutoTokenizer.from_pretrained(link)
        model = AutoModelForCausalLM.from_pretrained(link)
        
        # link = 'mrm8488/t5-base-finetuned-common_gen'
        # tokenizer = AutoTokenizer.from_pretrained(link)
        # model = AutoModelWithLMHead.from_pretrained(link)
        print(model)

        #prompt = " Sorry I'm late today because I saw a "+word + " and "
        # input_ids = tokenizer(paragraph+pieces[0]+word+pieces[1], return_tensors="pt").input_ids
        # input_ids = tokenizer(fullsentence, return_tensors="pt").input_ids
        input_ids = tokenizer.encode(fullsentence, return_tensors='pt')


        # generate up to 30 tokens
        outputs = model.generate(
          input_ids, 
          max_length=50, 
          num_beams=5, 
          no_repeat_ngram_size=2, 
          num_return_sequences=5, 
          early_stopping=True
        )
        # sentence = tokenizer.batch_decode(outputs, skip_special_tokens=True, )
        sentence = tokenizer.decode(outputs[0], skip_special_tokens=True, )
        fullsentence=sentence[0]
        fullsentence=sentence
        
        if (line_num ==len(lines)-1):
            sentence_prompt=". And well, that's why I'm late."
        else:
            line_num+=1
            pieces = lines[line_num].split("_")
            sentence_prompt=". " + pieces[0]


        paragraph+=fullsentence
        return render_template(
            'index.html',
            user=current_user,
            sentence=paragraph+sentence_prompt
        )
'''

@api.route('/sentence', methods=['GET', 'POST'])
def get_sentence():
    global line_num
    global paragraph
    global prevsentence
    showSpinner = True
    pieces = lines[line_num].split("_")
    paragraph+=prevsentence

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
        fullsentence = pieces[0] + word
        prompt1 = pieces[0]
        fullsentence_len = len(fullsentence)
        print(word)

        tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
        model = GPT2LMHeadModel.from_pretrained("gpt2", pad_token_id=tokenizer.eos_token_id)

        # model = AutoModelForCausalLM.from_pretrained("gpt2")
        #link = 'mrm8488/diltilgpt2-finetuned-bookcopus-10'
        # tokenizer = AutoTokenizer.from_pretrained(link)
        # model = AutoModelForCausalLM.from_pretrained(link)
        
       
        #prompt = " Sorry I'm late today because I saw a "+word + " and "
        # input_ids = tokenizer(fullsentence, return_tensors="pt").input_ids
        input_ids = tokenizer.encode(fullsentence, return_tensors='pt')

        # generate up to 30 tokens
        # outputs = model.generate(input_ids, do_sample=False, max_length=30)
        # outputs = model.generate(
        #   input_ids, 
        #   max_length=50, 
        #   num_beams=5, 
        #   no_repeat_ngram_size=2, 
        #   num_return_sequences=5, 
        #   early_stopping=True
        # )

        
        outputs = model.generate(
          input_ids, 
          do_sample=True,
          max_length=50, 
          top_p=0.95,
          top_k=0,
          num_return_sequences=3
        )
        # sentence = tokenizer.batch_decode(outputs, skip_special_tokens=True)
        sentence = tokenizer.decode(outputs[0], skip_special_tokens=True)
        sentencesplit = ".".join(sentence.split(".")[:-1])
        finalsentence=sentencesplit[fullsentence_len:]+". "

        prevsentence = sentencesplit+". "

        if (line_num ==len(lines)-1):
            sentence_prompt=". And well, that's why I'm late."
        else:
            line_num+=1
            pieces = lines[line_num].split("_")
            sentence_prompt=pieces[0]
        
        showSpinner=False
        return render_template(
            'index.html',
            user=current_user,
            sentence=paragraph+prompt1,
            word = word,
            end_prompt = finalsentence+sentence_prompt
        )


@api.route('/home')
def my_home():
    global paragraph
    sentencetosend=pieces[0]
    return render_template(
        'index.html',
        user=current_user,
        end_prompt=sentencetosend
    )

