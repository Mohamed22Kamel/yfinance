from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate ,login , logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django import forms
from django.forms import ModelForm, ValidationError
from django.contrib.auth import  authenticate , get_user_model
from .forms import UserRegisterForm , LoginForm ,ProfilePicForm
from .models import Profile
from .chat import bot_answer
def home(request):
    return render(request , 'Invest/welcomepage.html' )

def join(request):

    if request.method == "POST": 
     
        form = UserRegisterForm(request.POST)
        password = request.POST.get('password1') 
        confirmpassword = request.POST.get('password2')
        email = request.POST.get('email')

        if password != confirmpassword:
           
            messages.error(request,"password doesn't match")
            return render(request , 'Invest/signup.html' , {'form' : form })
        
        if form.is_valid():
           
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            confirmpassword = form.cleaned_data.get('password2')
            return redirect('login_page')

        else : 
            messages.error(request,form.errors)
 
           
    else: 
        form = UserCreationForm() 
        
    return render(request , 'Invest/signup.html' , {'form' : form })

    


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request , username=username , password =password)
      
        if user is not None :
           login(request ,user)
           return redirect('dashboard')
        else:
            return redirect('login_page')
       
    else :
        messages.error(request,f'Invalid username or password')
        return render(request ,'Invest/login.html')

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
    if request.method == 'POST':
        user = User.objects.get(id=request.user.id)
        profile = Profile.objects.get(user_id =request.user.id)
        user_form = UserRegisterForm(request.POST or None , request.FILES or None,instance = user) 
        profile_form = ProfilePicForm(request.POST or None ,request.FILES or None ,instance = profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('dashboard')   
    return render (request , 'Invest/edit.html')

def delete(request):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user)
        user.delete()
        return redirect('invest-home')
    return render (request , 'Invest/delete.html')


def learn(request):
    return render (request ,'Invest/learnmore.html')

def chat(request):

    if request.method == "POST":
        message = request.POST.get("message")
        response = bot_answer(message)
        return render(request ,"Invest/chat.html", {"message":message , 'response': response})
    else : 
        print("no post ")
    return render (request ,'Invest/chat.html')


def homePage(request):
  
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=request.user.id)
        return render (request , "Invest/home.html" , {"profile":profile} )
    else :
        return render (request ,'Invest/login.html') 
    

def logout_user(request):
    logout(request)
    return redirect('join')

     
    