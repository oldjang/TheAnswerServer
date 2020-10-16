from django.shortcuts import render
from django.shortcuts import HttpResponse
import json


# Create your views here.
def register(request):
    user_file = open("user.json")
    user_data = json.load(user_file)
    user_file.close()
    count = len(user_data)

    username = ""
    password = ""
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

    flag = True
    for user in user_data:
        if user['name'] == username:
            flag = False
    if flag:
        user_data.append({'name': username, 'password': password, "uid": count + 1})
        user_file = open("user.json", 'w')
        user_file.write(json.dumps(user_data))
        return HttpResponse(count + 1)
    else:
        return HttpResponse(0)


def login(request):
    user_file = open("user.json")
    user_data = json.load(user_file)
    user_file.close()

    username = ""
    password = ""
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

    print(username,password)

    uid = 0
    for user in user_data:
        if user['name'] == username and user['password'] == password:
            uid = user['uid']
    return HttpResponse(uid)


def add_question(request):
    user_file = open("user.json")
    user_data = json.load(user_file)
    user_file.close()

    uid = 0
    password = ""
    title = ""
    text = ""
    if request.method == 'POST':
        uid = request.POST.get('uid', None)
        password = request.POST.get('password', None)
        title = request.POST.get('title', None)
        text = request.POST.get('text', None)

    if user_data[int(uid) - 1]['password'] == str(password):
        question_file = open("question.json")
        question_data = json.load(question_file)
        question_file.close()
        count = len(question_data)
        now_question = {"qid": count + 1, "uid": uid, "title": title, "text": text}
        question_data.append(now_question)

        question_file = open("question.json", "w")
        question_file.write(json.dumps(question_data))
        question_file.close()
        return HttpResponse(json.dumps(now_question), content_type='application/json')
    else:
        return HttpResponse()

def question_list(request):
    user_file = open("user.json")
    user_data = json.load(user_file)
    user_file.close()

    uid = 0
    password = ""
    if request.method == 'POST':
        uid = request.POST.get('uid', None)
        password = request.POST.get('password', None)

    print(uid,password)

    if user_data[int(uid) - 1]['password'] == str(password):
        question_file = open("question.json")
        question_data = json.load(question_file)
        question_file.close()

        return HttpResponse(json.dumps(question_data), content_type='application/json')
    else:
        return HttpResponse()
