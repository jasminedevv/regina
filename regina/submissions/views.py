from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from django.http import HttpResponse

from .models import Submission
from django.contrib.auth.models import User

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