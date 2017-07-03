from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Profile
from .models import Budget
from django.views.decorators.csrf import csrf_exempt
import json
import time

# Create your views here.
@csrf_exempt 
def budget(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_id = data["userid"]
        
        budget_value = Budget.objects.values().filter(userid = user_id)

        if len(budget_value)==0 :
            return HttpResponse("no record")
        budget_all = Budget.objects.all().filter(userid = user_id)
        for item in budget_all :
            upgradetime = item.upgradetime
            if time.time()-upgradetime >2592000:
                item.delete()
                return HttpResponse("no record")
            else:
                rest = budget_value[0]["rest"]
                return HttpResponse(str(rest))

@csrf_exempt
def addbudget(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_id = data["userid"]
        if len(user_id)>1:
            new_budget = data["newbudget"]    
            _budget = Budget()
            _budget.userid = user_id
            _budget.rest = new_budget
            _budget.upgradetime = int(time.time())
            _budget.save()
        
            return HttpResponse("succeed")  
            
        else:
            return HttpResponse("fail")  

    else:
        return HttpResponse("fail")        