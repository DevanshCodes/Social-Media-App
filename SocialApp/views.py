from django.shortcuts import render,redirect,HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.
'''
def IndexLogIn(request):
    username=request.POST.get('username')
    password=request.POST.get('password')
    user = authenticate(request, username = username, password = password)
    if user is not None:
        login(request,user)
        return redirect('home')
    return render(request,'SocialApp/login.html',) #This is for not default '''

def home(request):
    return render(request,'SocialApp/home.html')

def logout_view(request):
    logout(request)

@login_required(login_url="/login")

def profile(request):
    username = User.username
    
    context = {
        'username':username,
    }
    return render(request,'SocialApp/profile.html',context)

