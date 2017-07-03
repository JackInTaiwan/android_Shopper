# --*-- coding:UTF-8 --*--
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .models import Product
from shopperProfile.models import Budget
import json
import time
from random import *

# Create your views here.
@csrf_exempt
def getphoto(request):
    if(request.method == "POST"):
        print "here"
        print str(request.body)
        return HttpResponse("failed")
    else:
        print "here2"
        return HttpResponse("failed")
        
@csrf_exempt
def uploadimg(request):
    if(request.method =="POST"):
        print "use!!"
        data = json.loads(request.body)
        seller = data["product_seller"]
        sellerid = data["product_sellerid"]
        print "use2"
        name = data["product_name"]
        print "use3"
        attr = data["product_attr"]
        price = data["product_price"]
        print "use4"
        img = data["product_img"]
        print "use5"
        uptime = int(time.time())
        print str(len(img))
        
        product = Product()
        product.seller = seller
        product.sellerid = sellerid
        product.product_name = name
        product.product_attr = attr
        product.product_price = price
        product.product_img = img
        product.product_uploadtime = uptime

        product.save()
        print str(product)
        return HttpResponse("succeed")
    else:
        return HttpResponse("failed2!")


@csrf_exempt        
def sellergetproduct(request):
    if(request.method == "POST"):
        data = json.loads(request.body)
        order = data["order"]
        pro_sellerid = data["product_sellerid"]
        product_value = Product.objects.values().filter(sellerid=pro_sellerid)
        print type(product_value)
        
        print type(Product.objects.values())
        
        product_dic = [item for item in product_value]
        if order < len(product_dic):
            print str(order)+"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
            #print str(product_dic[order])
            print "-------------------------------------------------"
            print "-------------------------------------------------"
            return HttpResponse(json.dumps(product_dic[order]))
        else:
            return HttpResponse("loadover")
            
    else:
        print "false!"
        return HttpResponse("loadover") 
        

@csrf_exempt 
def sellerremoveproduct(request):
    if(request.method =="POST"):
        data = json.loads(request.body)
        sellerid = data["product_sellerid"]
        uploadtime = data["product_uploadtime"]
        #下面要用objects.all().filter(~)然後進去delete()才可以!!不可以用objects.value().filter(~)
        product_value = Product.objects.all().filter(sellerid=sellerid,product_uploadtime=uploadtime)
        for entry in product_value:
            entry.delete()
        return "succeed remove"
        
        
@csrf_exempt 
def buyergetproduct(request):
    if(request.method == "POST"):
        data = json.loads(request.body)
        #get第幾頁
        page = data["page"]
        print page
        selected_strlist=[]
        #取出上傳的搜尋條件
        for item in data:
            #print type(data[item])
            if type(data[item]) is unicode:
                selected_strlist.append(data[item])
        #利用搜尋條件抓資料
        product_value = Product.objects.values()    #一定要用values()不可all()
        product_value_final=[]
        for item in product_value:
            if item["product_attr"] in selected_strlist:
                item["product_img"]=""    #此方式不會改到資料庫資料放心!為了傳送json時別太浪費空間所以歸零
                #print str(item)
                product_value_final.append(item)

        product_data = [item for item in product_value_final] #一定要轉成list
        
        #處理第幾頁的問題(每頁20筆)
        if (page >= 1) :
            print "!!!!!!!!!!!!!!!!!!!!!!!!"
            print "!!!!!!!!!!!!!!!!!!!!!!!!"
            print page 
            total = len(product_data)
            if (total>=(page*20)):
                product_data = product_data[20*(page-1):20*page]
            else :
                product_data = product_data[20*(page-1):total]
                print
            

        
        return  HttpResponse(json.dumps(product_data)) 

    return HttpResponse("succeed") 
    
    
@csrf_exempt
def getproductdetail(request):
    if (request.method=="POST"):
        data = json.loads(request.body)
        sellerid = data["sellerid"]
        uploadtime = data["product_uploadtime"]   
        product_value = Product.objects.values().filter(sellerid=sellerid,product_uploadtime=uploadtime)
        product_data = product_value[0]
        if len(product_data) >0 :
            return HttpResponse(json.dumps(product_data))
  
    return HttpResponse("fail")
    

@csrf_exempt
def buyer(request):     
    if (request.method == "POST"):
        data = json.loads(request.body)
        
        sellerid = data["sellerid"]
        uploadtime = data["product_uploadtime"]
        buyer = data["product_buyer"]   
        buyerid = data["product_buyerid"]

        product_value = Product.objects.all().filter(sellerid=sellerid,product_uploadtime=uploadtime)
        budget_value = Budget.objects.all().filter(userid = buyerid)

        
        for item in product_value:      #一定要用這個方式,不能用product_value[0]去叫= =
            if item.product_buyerid==0:

              for budget in budget_value:

                if (item.product_price<=budget.rest):
                    item.product_buyerid = buyerid
                    item.product_buyer = buyer
                    budget.rest += -item.product_price
                    
                    budget.save()
                    item.save()

                    result = {"result":1}
                    return HttpResponse(json.dumps(result))
                else:
                    result = {"result":2,"rest":budget.rest}

                    return HttpResponse(json.dumps(result))
            else :  
                result = {"result":0}    
                return HttpResponse(json.dumps(result))
    result = {"result":0}    
    return HttpResponse(json.dumps(result))
        
@csrf_exempt
def buyerhobby(request):
    if (request.method == "POST"):
        data = json.loads(request.body)

        a, b, c, d, e = data["a"], data["b"], data["c"], data["d"], data["e"]
        ap, bp, cp, dp, ep = data["A"], data["B"], data["C"], data["D"], data["E"]
        money = data["MONEY"]
        close = data["CLOSE"]
        num = data["NUM"]

        product_value_a1 = Product.objects.values().filter(product_attr=a)
        product_value_a = []
        for item in product_value_a1:
            if (item["product_price"] <= money) and (item["product_buyerid"]==0):
                item["product_img"]=""
                product_value_a.append(item)
        product_value_b1 = Product.objects.values().filter(product_attr=b)
        product_value_b = []
        for item in product_value_b1:
            if (item["product_price"] <= money) and (item["product_buyerid"]==0):
                item["product_img"]=""
                product_value_b.append(item)
        product_value_c1 = Product.objects.values().filter(product_attr=c)
        product_value_c = []
        for item in product_value_c1:
            if (item["product_price"] <= money) and (item["product_buyerid"]==0):
                item["product_img"]=""
                product_value_c.append(item)
        product_value_d1 = Product.objects.values().filter(product_attr=d)
        product_value_d = []
        for item in product_value_d1:
            if (item["product_price"] <= money) and (item["product_buyerid"]==0):
                item["product_img"]=""
                product_value_d.append(item)
        product_value_e1 = Product.objects.values().filter(product_attr=e)
        product_value_e = []
        for item in product_value_e1:
            if (item["product_price"] <= money) and (item["product_buyerid"]==0):
                item["product_img"]=""
                product_value_e.append(item)
        dic_product = {"a": product_value_a, "b": product_value_b, "c": product_value_c, "d": product_value_d,
                       "e": product_value_e}
        choose_samples = []
        total_useful_samples = 0
        if ap > 0:
            total_useful_samples += len(product_value_a)
            if len(product_value_a)>0:
                for i in range(ap):
                    choose_samples.append("a")
        if bp > 0:
            total_useful_samples += len(product_value_b)
            if len(product_value_b)>0:
                for i in range(bp):
                    choose_samples.append("b")
        if cp > 0:
            total_useful_samples += len(product_value_c)
            if len(product_value_c)>0:
                for i in range(cp):
                    choose_samples.append("c")
        if dp > 0:
            total_useful_samples += len(product_value_d)
            if len(product_value_d)>0:
                for i in range(dp):
                    choose_samples.append("d")
        if ep > 0:
            total_useful_samples += len(product_value_e)
            if len(product_value_e)>0:
                for i in range(ep):
                    choose_samples.append("e")

                # 宣告最後推薦清單set
        print choose_samples
        
        com_set = []
        if len(choose_samples) > 0:
            if 0 < total_useful_samples <= 2500:
                n = int(total_useful_samples ** 0.5)
            else:
                n = 50
            for i in range(n):
                com_subset = []
                totalprice = 0
                count =0
                limit_count = len(product_value_a)+len(product_value_b)+len(product_value_c)+len(product_value_d)+len(product_value_e)
                print "!!!!!!!!!!!!!!"+str(i)
                while ((money > totalprice)and(count<limit_count)):
                    x = randint(0, len(choose_samples) - 1)
                    print x
                    print choose_samples[x]
                    print "len   "+str(len(dic_product[choose_samples[x]]))
                    y = randint(0, len(dic_product[choose_samples[x]])-1)
                    price = dic_product[choose_samples[x]][y]["product_price"]
                    if dic_product[choose_samples[x]][y] not in com_subset:
                        com_subset.append(dic_product[choose_samples[x]][y])
                        totalprice += price
                        count+=1
                if com_subset != []:
                    com_subset.pop()
                    if (com_subset !=[]) and (com_subset not in com_set):
                        com_set.append(com_subset)

        if com_set == []:
            print "fail"
            return HttpResponse("fail")
        else:
            # 從清單中選出最佳推薦
            # close_index = (1-總價/money)close/100.0
            # num_index = 個數**2.0/(money**0.5)
            # best_index = close_index+num_index
            index_set = []
            for item in com_set:
                totalcost = 0
                totalnum = 0
                for items in item:
                    totalnum += 1
                    totalcost += items["product_price"]
                close_index = ((1 - totalcost / money) * close) / 100.0
                num_index = totalnum ** 2.0 / (money ** 0.5)
                index_set.append(close_index+num_index)
            print "all score!!!!!!!!!!!!!!!!!!!!!!!!!"
            print str(index_set)
            choose_index = 0
            best_index = 0
            for i in range(len(index_set)):
                if index_set[i] > best_index:
                    best_choose = i
                    best_index = index_set[i]

            final_best_list = com_set[i]
            json_final_best_list = json.dumps(final_best_list)
            print str(json_final_best_list)
            return HttpResponse(json_final_best_list)
                
            
        
        
        
        
