from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistraionForm
from django.http import HttpResponse
# Create your views here.
def login(request):
    return render(request, "user/login.html")

def register(request):
    if request.method == 'POST':
        form = UserRegistraionForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for { username }!')
            return redirect('blog-home')
    else:
        form = UserRegistraionForm()
    return render(request, "user/register.html", {'form' : form})

def profile(request):
    return HttpResponse('<h4>Profile page not ready</h4>')

def settings(request):
    return HttpResponse('<h4>Settings page not ready</h4>')