from django.shortcuts import render
from django.http import HttpResponse
from .models import posts

# Create your views here.
content = {
    'posts': posts.objects.all()
 }
def home(request):
    return render(request, "blog/home.html", content)

def login(request):
    return render(request, "blog/login.html")

def register(request):
    return render(request, "blog/register.html")