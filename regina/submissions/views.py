from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from django.http import HttpResponse

from .models import Submission
from .forms import SubmissionForm

from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm

# no clue what this does
from django.forms import modelformset_factory

# Create your views here.

def home(request):
    user = request.user
    if user.is_authenticated:
        user = User.objects.get(username=request.user.username)
        user_submissions = Submission.objects.filter(user=user)

        return render(request, 'home.html', {'user':user, 'submissions':user_submissions})
    else:
        return redirect('accounts/login/')


def submit(request):
    user = request.user
    if user.is_authenticated:
        if request.method == 'GET':
            form = SubmissionForm()
            return render(request, 'submit.html', {'user':user, 'form':form})
        elif request.method == 'POST':
            form = SubmissionForm(request.POST)
            if form.is_valid():
                submission = form.save()
                print(request.user.username)
                submission.user = User.objects.get(username=request.user.username)
                print(submission.user.username)
                submission.save()
                return redirect('/')
            else:
                error = "There was a problem with your form. Please try again."
                return render(request, 'submit.html', {'user':user, 'form':form, 'error': error})
    else:
        return redirect('accounts/login/')

# not wired up yet, probably doesn't work
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
