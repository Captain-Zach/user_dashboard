import bcrypt
from django.contrib import messages
from django.shortcuts import HttpResponse, redirect, render
import time

# from app_one.models import Comment, Message, User

# Create your views here.
def index(request):
    


    return render(request, 'index.html')