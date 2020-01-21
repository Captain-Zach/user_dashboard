import bcrypt
from django.contrib import messages
from django.shortcuts import HttpResponse, redirect, render
import time

from app_one.models import User, Comment, Message

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

###################WALL BEGINS####################################################

def the_wall(request, user_id):
    all_messages = Message.objects.all().order_by('-created_at')
    target_user = User.objects.get(id=user_id)
    target_messages = target_user.user_wall.all().order_by('-created_at')
    current_user = User.objects.get(id=request.session['user_id'])
    # Access then store data in context
    context = {
        'all_messages': target_messages,
        'target_user':target_user,
        'current_user':current_user,

    }
    return render(request, "wall.html", context)


def create_message(request):
    content = request.POST['content']
    target_user = User.objects.get(id=request.POST['on_which_wall'])
    user = User.objects.get(id=request.session['user_id'])
    new_message = Message.objects.create(content=content, made_by=user, on_which_wall=target_user)
    print("new message created", new_message)
    return redirect('/users/show/'+str(target_user.id))

def create_comment(request):
    #Validate
    content = request.POST['content']
    user = User.objects.get(id=request.session['user_id'])
    message = Message.objects.get(id=request.POST['message_id'])
    newComment = Comment.objects.create(content=content, on_message=message, made_by=user)
    print('New comment created,', newComment)
    print(newComment.made_by.name)
    print(newComment.created_at)
    print(newComment.content)
    return redirect('/users/show/'+request.POST['user_id'])

#################################################################################

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
    #need validations
    name = request.POST['name']
    alias = request.POST['alias']
    email = request.POST['email']
    password = request.POST['password']
    new_user = User.objects.create(name=name, alias=alias, email=email, password=password) 

    return redirect('/dashboard/admin')

def make_changes(request, user_id):
    target_user = User.objects.get(id=user_id)
    #need validation

    #make changes here
    target_user.name = request.POST['name']
    target_user.alias = request.POST['alias']
    target_user.email = request.POST['email']
    target_user.user_level = int(request.POST['user_level'])
    target_user.save()
    return redirect('/dashboard/admin')

def make_changesx(request):
    user = User.objects.get(id=request.session['user_id'])
    #need validation
    user.name = request.POST['name']
    user.alias = request.POST['alias']
    user.email = request.POST['email']
    user.desc = request.POST['desc']
    user.save()
    #make normal changes here
    #need validation
    return redirect('/dashboard')

def change_password(request, user_id):
    #make changes here
    user = User.objects.get(id=user_id)
    user.password = request.POST['password']
    user.save()
    #need validation
    return redirect('/dashboard')


def change_passwordx(request):
    #for users to change their own password.  Bad panic naming convention
    user = User.objects.get(id=request.session['user_id'])
    user.password = request.POST['password']
    user.save()
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
    user = User.objects.get(id=user_id)
    user.delete()
    # check if user still exists.  If self delete, log them out
    return redirect('/dashboard')