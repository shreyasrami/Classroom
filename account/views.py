from django.shortcuts import render
import re

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.views import View
from .forms import Radio
from .models import User,Teacher,Student

class Register(View):
   
    
    def get(self,request,*args,**kwargs):
        
        form = Radio()
        context = {
            'form' : form
        }
        return render(request,'register.html',context)


    def post(self,request,*args,**kwargs):
        
        form = Radio(request.POST)
        if form.is_valid():
            choice = form.cleaned_data['choice']
           
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        department = request.POST.get('department') 
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')


        if password1 == password2 :
            if User.objects.filter(username__exact=username).exists() : 
                err = 'Username already taken'
                    
            elif User.objects.filter(email__exact=email).exists() :
                err = 'Email already taken'
                    
            else:
                if choice == 'teacher':
                    subject = request.POST.get('subject')
                    user = Teacher.objects.create_user(first_name=first_name,last_name=last_name,username=username,
                    department=department,email=email,password=password1,subject=subject,is_teacher=True)
                    user.is_teacher = True
                    user.subject=subject
                else:
                    sap = request.POST.get('sap')
                    pattern = r"^60004[12][04-9][0-9][0-9][0-9][0-9]$"
                    if Student.objects.filter(sap_id__exact=sap).exists():
                        context = {
                            'message' : 'Student with Sap ID : '+sap+'is already registered with us',
                            'form' : form
                        }
                        return render(request,'register.html',context)
                    elif not re.match(pattern,sap):
                        context = {
                            'message' : 'Please enter a valid Sap ID',
                            'form' : form
                        }
                        return render(request,'register.html',context)
                    else:
                        div = request.POST.get('div')
                        user = Student.objects.create_user(first_name=first_name,last_name=last_name,username=username,
                        department=department,email=email,password=password1,sap_id=sap,division=div,is_student=True)
                    
                user.save()
                context = {
                    'username'  : username,
                    'choice'    : choice,
                    'message'   : "User Successfully created"
                }
                return render(request,'login.html',context)
                
        else:
            err = 'Passwords does not match'
        
        context = {
            'message' : err ,
            'form' : form
        }
        
        return render(request,'register.html',context)

            
            
        

class Login(View):

    def get(self,request,*args,**kwargs):
        
        return render(request,'login.html')

    
    def post(self,request,*args,**kwargs):
        email = request.POST['email']
        password = request.POST['password']
        
        user = auth.authenticate(email=email,password=password)
                
        if user is not None:
            auth.login(request,user)
            return render(request,'home.html')

        else:
            context = {
                'message' : 'Invalid Email or Password'
            }
            return render(request,'login.html',context)

        


class Logout(View):
    def get(self,request,*args,**kwargs):
        auth.logout(request)
        return redirect('/')
