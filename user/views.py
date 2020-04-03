from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistraionForm, UserUpdateForm, ProfileUpdateForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

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

@login_required
def profile(request):
    return render(request, 'user/profile.html', {
        # 'User': request.User
        })

@login_required
def settings(request):
    return HttpResponse('<h4>Settings page not ready</h4>')