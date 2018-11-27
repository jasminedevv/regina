from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from django.http import HttpResponse

from .models import Submission
from .forms import SubmissionForm

from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm

# no clue what this does
from django.forms import modelformset_factory

def manage_authors(request):
    AuthorFormSet = modelformset_factory(Author, fields=('name', 'title'))
    if request.method == 'POST':
        formset = AuthorFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            # do something.
    else:
        formset = AuthorFormSet()
    return render(request, 'manage_authors.html', {'formset': formset})

# Create your views here.

def home(request):
    user = request.user
    if user.is_authenticated:
        return render(request, 'home.html', {'user':user})
    else:
        return redirect('accounts/login/')

# def new_submission(request):
#     form = SubmissionForm(request.POST)
#     if form.is_valid():
#         submission = form.save(commit=False)
#         submission.user = request.user
#         submission.save()
#         return True
#     else:
#         return False

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

class Accounts(UserCreationForm):
    '''
        potentially not needed.
    '''


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
