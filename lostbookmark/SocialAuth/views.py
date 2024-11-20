from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return render(request, 'SocialAuth/index.html')
# step 3 : create a login view


def login(request):
    return render(request, 'SocialAuth/login.html')


def dashboard(request):
    return render(request, 'SocialAuth/dashboard.html')


def clean_bookmark(request):
    return HttpResponse("Clean Bookmark")
