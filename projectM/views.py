from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def login(request):
    return render(request,'login.html')

def signup(request):
    return render(request,'signup.html')

def error_404(request,exception):
    return render(request,'error.html',{'data1':'page not found'})
