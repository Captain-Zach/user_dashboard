import bcrypt
from django.contrib import messages
from django.shortcuts import HttpResponse, redirect, render
import time

from app_one.models import User #Comment, Message,

# Create your views here.
def index(request):
    return render(request, 'index.html')

def signin(request):
    return render(request, "sign_in.html")

def register(request):
    return render(request, "register.html")

def dashboard(request):
    user = User.objects.get(id=request.session['user_id'])
    if user.user_level == 9:
        return redirect('/dashboard/admin')
    all_users = User.objects.all()


    context = {
        'all_users': all_users
    }

    return render(request, "user_dashboard.html", context)

def admin_dashboard(request):
    all_users = User.objects.all()


    context = {
        'all_users': all_users
    }
    return render(request, "admin_dashboard.html", context)

def users_new(request):
    return render(request, "add_user.html")

def the_wall(request, user_id):
    return render(request, "wall.html")

def edit_user(request, user_id):
    target_user = User.objects.get(id=user_id)
    context ={
        'target_user': target_user
    }

    return render(request, "admin_edit.html", context)

def edit_self(request):
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'user': user
    }
    return render(request, "user_edit.html", context)

def log_in(request):
    email = request.POST['email']
    user = User.objects.get(email=email)
    request.session['user_id'] = user.id
    if user.user_level == 9:
        return redirect('/dashboard/admin')
    return redirect('/dashboard')

def log_out(request):
    request.session.flush()
    return redirect('/')

def create_user(request):
    # loading my vars
    name = request.POST['name']
    alias = request.POST['alias']
    email = request.POST['email']
    password = request.POST['password']
    user_level = 9
    # Checking to see if this is the first user being created.
    all_users = User.objects.all()
    if len(all_users) < 1:
        # do create logic here
        new_user = User.objects.create(name=name, alias=alias, email=email, password=password, user_level=user_level) 
        request.session['user_id'] = new_user.id
        return redirect('/dashboard/admin')
    else:
        new_user = User.objects.create(name=name, alias=alias, email=email, password=password) 
        request.session['user_id'] = new_user.id
        return redirect('/dashboard')

def create_user_admin(request):
    
    return redirect('/dashboard/admin')

def make_changes(request, user_id):
    target_user = User.objects.get(id=user_id)
    #make changes here
    #need validation
    return redirect('/dashboard/admin')

def make_changesx(request):
    user = User.objects.get(id=request.session['user_id'])
    

    #make normal changes here
    #need validation
    return redirect('/dashboard')

def change_password(request):
    #make changes here
    #need validation
    return redirect('/dashboard')


def change_passwordx(request):
    user = User.objects.get(id=request.session['user_id'])
    #make password changes here
    #need validation
    return redirect('/dashboard')

def confirmation(request, user_id):
    user = User.objects.get(id=user_id)
    context = {
        'user': user
    }
    return render(request, "confirmation.html", context)

def delete_user(request, user_id):
    # check if user still exists.  If self delete, log them out
    return redirect('/dashboard')