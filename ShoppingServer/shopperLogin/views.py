from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Account
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
import time

# Create your views here.
@csrf_exempt
def login(request):
    if(request.method == "POST"):
        data = json.loads(request.body)
        account_name = data["theaccount"]
        account_passwd = data["thepasswd"]
        print account_name, account_passwd
        return HttpResponse("received")
