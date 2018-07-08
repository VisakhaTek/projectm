from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import authenticate

#models
from django.contrib.auth.models import User

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
    	var1 = request.POST.get('password')
    	var2 = request.POST.get('reenter_password')
    	print(var1,var2)
    	
    	if var1==var2:
            user = User()
            user.username = request.POST.get('username')
            user.email = request.POST.get('username')
            user.password = request.POST.get('password')
            print(user.email)
            user.save()
            var3 = 'Success'
    	else:
            var3 = 'Error'
    	return HttpResponse(var3)

def error_404(request,exception):
    return render(request,'error.html',{'data1':'page not found'})
