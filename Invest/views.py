from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django import forms
from django.forms import ModelForm, ValidationError
from .forms import UserRegisterForm , LoginForm
from django.contrib.auth import  authenticate , get_user_model

def home(request):
    return render(request , 'Invest/welcomepage.html' )

def join(request):

    if request.method == "POST": 
        
        form = UserRegisterForm(request.POST)

        password = request.POST.get('password1') 

        confirmpassword = request.POST.get('password2')

        email = request.POST.get('email')

        print(email)
        if password != confirmpassword:
           
            messages.error(request,"password doesn't match")
            return render(request , 'Invest/signup.html' , {'form' : form })
         #       raise forms.ValidationError("Passwords must match!") 

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'account created {username}')
            return render(request , 'Invest/home.html' , {'form' : form }) 

        else : 
            messages.error(request,form.errors)
            
            #username = form.cleaned_data.get('username')
            
    
            print('*' * 30 )
           
    else: 
        form = UserCreationForm() 
        print('else' * 30 )
    return render(request , 'Invest/signup.html' , {'form' : form })

    
def homePage(request):
    return render(request , 'Invest/home.html' )

def login_page(request):

    if request.method == 'GET':
        form = LoginForm()
        return render(request,'Invest/login.html', {'form': form})
    
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
      
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
         
            user = authenticate(request,username=username,password=password)
            print(user)
            if user:
               
                messages.success(request,f'Hi {username.title()}, welcome back!')
                return render(request , 'Invest/home.html' )
        
        # form is not valid or user is not authenticated
        messages.error(request,f'Invalid username or password')
        return render(request,'Invest/login.html',{'form': form})


def reset_page(request):
    if request.method == 'POST': 
        username = request.POST.get('username')
        password = request.POST.get('password1')
        confirmpassword = request.POST.get('password2')
        if get_user_model().objects.filter(username=username):
            if password == confirmpassword : 
                user = User.objects.get(
               
                username=username,  
            
                )      
                user.set_password(password)
                user.save()
                return render(request , 'Invest/done.html')
    return render(request , 'Invest/reset.html')

def done(request):
    
    return render(request ,'Invest/done.html')


def edit(request):
    
    return render (request , 'Invest/edit.html')


     
    