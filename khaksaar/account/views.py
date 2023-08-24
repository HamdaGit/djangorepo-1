from django.shortcuts import render

# Create your views here.
def account(request):
    return render(request, 'profile.html' )

def signup(request):
    return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')