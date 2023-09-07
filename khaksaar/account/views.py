from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login


# Create your views here.
def account(request):
    return render(request, 'profile.html' )


User = get_user_model()
@csrf_protect
def signup(request):
    if request.method == 'POST':
      print(request.POST)
      form = CustomUserCreationForm(request.POST)
      print(form.is_valid())
      if form.is_valid():
        form.save()
        return redirect(reverse_lazy('home'))
    else:
      form = CustomUserCreationForm()
    return render(request, "signup.html", {'form': form})

def login(request):
     
     return render(request, 'login.html')