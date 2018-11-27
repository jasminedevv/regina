from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from django.http import HttpResponse

from .models import Submission
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def home(request):
    user = request.user
    if user.is_authenticated:
        return render(request, 'home.html', {'user':user})
    else:
        return redirect('accounts/login/')

def submit(request):
    user = request.user
    if user.is_authenticated:
        return render(request, 'submit.html', {'user':user})
    else:
        return redirect('accounts/login/')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})