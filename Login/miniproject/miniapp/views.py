from django.shortcuts import render,redirect
from miniapp.models import User
from django.contrib import messages
from django.db import connection
from django.contrib.auth import authenticate, login
from sre_constants import BRANCH
from typing import final
from django.shortcuts import render
from miniapp.models import final_class

from django.contrib import messages
from django.db import connection
from miniapp.resources import app_finalReource
from tablib import Dataset
def simple_upload(request):
    if request.method == "POST":
        app_final_Reource= app_finalReource()
        dataset =Dataset()
        new_final_class= request.FILES['myfile']
        
        if not new_final_class.name.endswith("xlsx"):
           messages.info(request,"wrong format")
           return render(request,"upload.html")
        imported_data=dataset.load(new_final_class.read(),format='xlsx')
        for data in imported_data:
            value=final_class(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4],
                data[5],
                data[6],
                data[7],
          
                )
            value.save()    
    return render(request,'upload.html')
def home(request): 
    return render(request,'home.html')
def login(request):
    if request.method=='POST':
      try:
        Userdetails=User.objects.get(email=request.POST['email'],password=request.POST['password'])
        print("Username",Userdetails)
        request.session['email']=Userdetails.email
        return render(request,'home1.html')    
      except User.DoesNotExist as e:
        messages.success(request,'username/password invalid')
    return render(request, 'login.html')

def Userregistration(request):
    saverecord=User()
    if request.method=='POST':
        if request.POST.get('roll') and request.POST.get('fname') and request.POST.get('lname') and request.POST.get('email') and request.POST.get('password'): 
            saverecord.roll=request.POST.get('roll')
            saverecord.fname=request.POST.get('fname')
            saverecord.lname=request.POST.get('lname')
            saverecord.email=request.POST.get('email')
            saverecord.password=request.POST.get('password')
            saverecord.save()
            messages.success(request,"New User Registration details saved successfully")
          
    return render(request,'register.html')

def home1(request):
    return render(request,'home1.html')
def cse4(request):
    c4=final_class.objects.filter(year=4,branch='cse')
    return render(request,'show.html',{'c4':c4})
def cse3(request):
    c3=final_class.objects.filter(year=3,branch='cse')
    return render(request,'show.html',{'c3':c3})
def cse2(request):
    c2=final_class.objects.filter(year=2,branch='cse')
    return render(request,'show.html',{'c2':c2})
def cse1(request):
    c1=final_class.objects.filter(year=1,branch='cse')
    return render(request,'show.html',{'c1':c1})
def eee4(request):
    e4=final_class.objects.filter(year=4,branch='eee')
    return render(request,'show.html',{'e4':e4})
def eee3(request):
    e3=final_class.objects.filter(year=3,branch='eee')
    return render(request,'show.html',{'e3':e3})
def eee2(request):
    e2=final_class.objects.filter(year=2,branch='eee')
    return render(request,'show.html',{'e2':e2})
def eee1(request):
    e1=final_class.objects.filter(year=1,branch='eee')
    return render(request,'show.html',{'e1':e1})
def it4(request):
    i4=final_class.objects.filter(year=4,branch='it')
    return render(request,'show.html',{'i4':i4})
def it3(request):
    i3=final_class.objects.filter(year=3,branch='it')
    return render(request,'show.html',{'i3':i3})
def it2(request):
    i2=final_class.objects.filter(year=2,branch='it')
    return render(request,'show.html',{'i2':i2})
def it1(request):
    i1=final_class.objects.filter(year=1,branch='it')
    return render(request,'show.html',{'i1':i1})
def ece4(request):
    ec4=final_class.objects.filter(year=4,branch='ece')
    return render(request,'show.html',{'ec4':ec4})
def ece3(request):
    ec3=final_class.objects.filter(year=3,branch='ece')
    return render(request,'show.html',{'ec3':ec3})
def ece2(request):
    ec2=final_class.objects.filter(year=2,branch='ece')
    return render(request,'show.html',{'ec2':ec2})
def ece1(request):
    ec1=final_class.objects.filter(year=1,branch='ece')
    return render(request,'show.html',{'ec1':ec1})
def csm4(request):
    cs4=final_class.objects.filter(year=4,branch='csm')
    return render(request,'show.html',{'cs4':cs4})
def csm3(request):
    cs3=final_class.objects.filter(year=3,branch='csm')
    return render(request,'show.html',{'cs3':cs3})
def csm2(request):
    cs2=final_class.objects.filter(year=2,branch='csm')
    return render(request,'show.html',{'cs2':cs2})
def csm1(request):
    cs1=final_class.objects.filter(year=1,branch='csm')
    return render(request,'show.html',{'cs1':cs1})


def cse4rem(request):
    c4r=final_class.objects.filter(year=4,branch='cse',marks__lte=7)
    return render(request,'rem.html',{'c4r':c4r})
def cse3rem(request):
    c3r=final_class.objects.filter(year=3,branch='cse',marks__lte=7)
    return render(request,'rem.html',{'c3r':c3r})
def cse2rem(request):
    c2r=final_class.objects.filter(year=2,branch='cse',marks__lte=7)
    return render(request,'rem.html',{'c2r':c2r})
def cse1rem(request):
    c1r=final_class.objects.filter(year=1,branch='cse',marks__lte=7)
    return render(request,'rem.html',{'c1r':c1r})
def eee4rem(request):
    e4r=final_class.objects.filter(year=4,branch='eee',marks__lte=7)
    return render(request,'rem.html',{'e4r':e4r})
def eee3rem(request):
    e3r=final_class.objects.filter(year=3,branch='eee',marks__lte=7)
    return render(request,'rem.html',{'e3r':e3r})
def eee2rem(request):
    e2r=final_class.objects.filter(year=2,branch='eee',marks__lte=7)
    return render(request,'rem.html',{'e2r':e2r})
def eee1rem(request):
    e1r=final_class.objects.filter(year=1,branch='eee',marks__lte=7)
    return render(request,'rem.html',{'e1r':e1r})
def it4rem(request):
    i4r=final_class.objects.filter( year=4,branch='it',marks__lte=7)
    return render(request,'rem.html',{'i4r':i4r})
def it3rem(request):
    i3r=final_class.objects.filter(year=3,branch='it',marks__lte=7)
    return render(request,'rem.html',{'i3r':i3r})
def it2rem(request):
    i2r=final_class.objects.filter(year=2,branch='it',marks__lte=7)
    return render(request,'rem.html',{'i2r':i2r})
def it1rem(request):
    i1r=final_class.objects.filter(year=1,branch='it',marks__lte=7)
    return render(request,'rem.html',{'i1r':i1r})
def ece4rem(request):
    ec4r=final_class.objects.filter(year=4,branch='ece',marks__lte=7)
    return render(request,'rem.html',{'ec4r':ec4r})
def ece3rem(request):
    ec3r=final_class.objects.filter(year=3,branch='ece',marks__lte=7)
    return render(request,'rem.html',{'ec3r':ec3r})
def ece2rem(request):
    ec2r=final_class.objects.filter(year=2,branch='ece',marks__lte=7)
    return render(request,'rem.html',{'ec2r':ec2r})
def ece1rem(request):
    ec1r=final_class.objects.filter(year=1,branch='ece',marks__lte=7)
    return render(request,'rem.html',{'ec1r':ec1r})
def csm4rem(request):
    cs4r=final_class.objects.filter(year=4,branch='csm',marks__lte=7)
    return render(request,'rem.html',{'cs4r':cs4r})
def csm3rem(request):
    cs3r=final_class.objects.filter(year=3,branch='csm',marks__lte=7)
    return render(request,'rem.html',{'cs3r':cs3r})
def csm2rem(request):
    cs2r=final_class.objects.filter(year=2,branch='csm',marks__lte=7)
    return render(request,'rem.html',{'cs2r':cs2r})
def csm1rem(request):
    cs1r=final_class.objects.filter(year=1,branch='csm',marks__lte=7)
    return render(request,'rem.html',{'cs1r':cs1r})
def logout(request):
    try:
        del request.session['email']
    except:
        return render(request,'home.html')
    return render(request, 'home.html')