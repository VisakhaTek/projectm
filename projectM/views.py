from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

from manager.user_manager import UserManager

def home(request):
    return render(request,'home.html')

class Login(View):
    def get(self,request):
        return render(request,'login.html')
    def post(self,request,*args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username,password = password)
        print(user)
        if user is not None:
            return HttpResponse('Logged In') 
        else:
            return HttpResponse('Try Again') 

class Signup(View):

    def get(self, request, *args, **kwargs):
    	return render(request, 'signup.html')

    def post(self, request, *args, **kwargs):

        #Read POST data and create user. 
        username = request.POST.get('username')
        email = request.POST.get('username')
        password = request.POST.get('password')
        userManager = UserManager()
        userManager.addUser(username,password,email)

def error_404(request,exception):
    return render(request,'error.html',{'data1':'page not found'})
