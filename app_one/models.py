from __future__ import unicode_literals

import datetime
import re

import bcrypt
from django.db import models
from django.utils.timezone import utc


class MessageManager(models.Manager):
    pass

class CommentManager(models.Manager):
    pass

class UserManager(models.Manager):
    def login_validator(self, postData):
        errors = {}
        # Regex checks the format of the input.
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid Email address!"
        # a list of emails.  Should only ever go to one
        emailCheck = User.objects.filter(email=postData['email'])
        

        # define checks here
        # Checks for any matching emails.  We need one in order to get through
        if len(emailCheck) < 1:
            errors['email'] = "Email doesn't match any found in our records."
            print('email is bad')
        # if TU != None prevents exceptions in the case that an email is no good.
        target_user = emailCheck.first()
        if target_user != None:
            # compares hashed PWORDS
            if bcrypt.checkpw(postData['password'].encode(), target_user.password.encode()):
                pass
            else:
                errors['bad'] = "Your password was incorrect."
                print("the password is bad")
        return(errors)
        

    def basic_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['name']) < 2:
            errors['name'] = "First name is too short!"
        if len(postData['alias']) < 2:
            errors['alias'] = "Last name is too short!"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid Email address!"
        if len(postData['password']) < 8:
            errors['password'] = "Your password is too short dude!"
        if postData['password'] != postData['password_conf']:
            errors['password_conf'] = "Your password must match the confirmation!"
        return errors
    pass
# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=45)
    alias = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    desc = models.TextField(null=True)
    password = models.CharField(max_length=60)
    user_level = models.IntegerField(default = 1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Message(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    on_which_wall = models.ForeignKey(User, related_name="user_wall", on_delete=models.CASCADE)
    made_by = models.ForeignKey(User, related_name="messages", on_delete=models.CASCADE)
    objects = MessageManager()
    

class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    on_message = models.ForeignKey(Message, related_name="comments", on_delete=models.CASCADE)
    made_by = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
