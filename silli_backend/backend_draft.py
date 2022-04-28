from platform import java_ver
from urllib import response


lines=[]
with open('sentence-prompts.txt') as f:
    lines = f.readlines()
line_num=0
pieces = lines[line_num].split("_")
line_num+=1
sentencetosend=pieces[0]
#send this sentencetosend
#wait for response

function onsubmit:
    fullsentence=pieces[0]+response+pieces[1]
    sentencetosend=response+pieces[1]
    sentencetosend += model(fullsentence)
    #send this sentencetosend
    if (line_num ==len(lines)):
        sentencetosend="And well, that's why I'm late."
    else:
        pieces = lines[line_num].split("_")
        line_num+=1
        sentencetosend=pieces[0]
    #send this sentencetosend











for line in lines:
    pieces = line.split("_")
    sentencetosend=pieces[0]
    #send this sentencetosend
    #wait for response
    fullsentence=pieces[0]+response+pieces[1]
    sentencetosend=response+pieces[1]
    sentencetosend += model(fullsentence)
    #send this sentencetosend

sentencetosend="And well, that's why I'm late."
#send this sentencetosend