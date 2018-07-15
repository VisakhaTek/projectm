from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views import View

from manager.user_manager import UserManager

def home(request):
    return render(request,'home.html')

class Login(View):
    def get(self,request):
        return render(request,'login.html', {'show_signup':True})
    def post(self,request,*args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username,password = password)
        if user is not None:
            return HttpResponseRedirect(reverse('dealerhome'))
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
        return render(request,'login.html', {'show_signup':False})

def useradmin(request):
    return render(request,'useradmin.html')

def dealerhome(request):
    return render(request,'dealerhome.html')

def error_404(request,exception):
    return render(request,'error.html',{'data1':'page not found'})
