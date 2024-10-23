from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
# Create your views here.
def index(request):
    return render(request,'main/index.html')
def about(request):
    return render(request,'main/about.html')
def question(request):
    return render(request,'main/question.html')
def ask(request):
    return render(request,'main/ask.html')
def login(request):
    return render(request,'main/login.html')
def signup(request):
    return render(request,'main/signup.html')