from django.shortcuts import render
from django.shortcuts import HttpResponse
import json


# Create your views here.
def register(request):
    f_obj=open("user.json")
    x=json.load(f_obj)
    return HttpResponse(x)
