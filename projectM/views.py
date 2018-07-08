from django.shortcuts import render
from django.views import View

#models
from django.contrib.auth.models import User

def home(request):
    return render(request,'home.html')

def login(request):
    return render(request,'login.html')

class Signup(View):

    def get(self, request, *args, **kwargs):
    	return render(request, 'signup.html')

    def post(self, request, *args, **kwargs):
    	pass



def error_404(request,exception):
    return render(request,'error.html',{'data1':'page not found'})
