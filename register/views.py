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
    count = len(user_data)

    username = ""
    password = ""
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

    uid = 0
    for user in user_data:
        if user['name'] == username and user['password'] == password:
            uid = user['uid']
    return HttpResponse(uid)
