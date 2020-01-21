import bcrypt
from django.contrib import messages
from django.shortcuts import HttpResponse, redirect, render
import time

# from app_one.models import Comment, Message, User

# Create your views here.
def index(request):
    return render(request, 'index.html')

def signin(request):
    return render(request, "sign_in.html")

def register(request):
    return render(request, "register.html")

def dashboard(request):
    return render(request, "user_dashboard.html")

def admin_dashboard(request):
    return render(request, "admin_dashboard.html")

def users_new(request):
    return render(request, "add_user.html")

def the_wall(request):
    return render(request, "wall.html")

def edit_user(request):
    return render(request, "admin_edit.html")

def edit_self(request):
    return render(request, "user_edit.html")

def log_in(request):
    return redirect('/dashboard')

def log_out(request):
    return redirect('/')

def create_user(request):
    #create user here, same route
    #pass in linkback
    return redirect('/dashboard')