from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views.decorators.csrf import ensure_csrf_cookie



# Create your views here.
def account(request):
    return render(request, 'profile.html' )


@ensure_csrf_cookie
def signup(request):
    if request.method == 'POST':
      form = CustomUserCreationForm(request.POST)
      if form.is_valid():
        form.save()
          
      return redirect(reverse_lazy('home'))
    else:
      form = CustomUserCreationForm()
    return render(request, "signup.html", {'form': form})

def login(request):
    return render(request, 'login.html')