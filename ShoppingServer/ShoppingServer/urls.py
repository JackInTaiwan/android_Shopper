"""ShoppingServer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
import django.views
import shopperLogin.views
import shopperManage.views
import shopperProfile.views



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^shopperLogin/$', shopperLogin.views.login),
    url(r'^uploadimg/$',shopperManage.views.uploadimg),
    url(r'^sellergetproduct/$', shopperManage.views.sellergetproduct),
    url(r'^sellerremoveproduct/$', shopperManage.views.sellerremoveproduct),
    url(r'^buyergetproduct/$', shopperManage.views.buyergetproduct),
    url(r'^getproductdetail/$', shopperManage.views.getproductdetail),
    url(r'^buyer/$', shopperManage.views.buyer),
    url(r'^buyerhobby/$', shopperManage.views.buyerhobby),
    url(r'^budget/$', shopperProfile.views.budget),
    url(r'^addbudget/$', shopperProfile.views.addbudget),

]
