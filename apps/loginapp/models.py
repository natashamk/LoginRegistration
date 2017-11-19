from __future__ import unicode_literals

from django.db import models

import re, bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')
PWD_REGEX = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).+$')

# Create your models here.
class UserManager(models.Manager):
    def basic_validate(self, postdata):
        errors = []
        if len(postdata['fname']) < 2:
            error.append("Please enter a valid first name")
        elif not NAME_REGEX.match(postdata['fname']):
            errors.append('Invalid first name')
        if len(postdata['lname']) < 2:
            error.append("Please enter a valid last name")
        elif not NAME_REGEX.match(postdata['lname']):
            errors.append('Invalid last name')
        if len(postdata['email']) < 1:
            error.append("Email cannot be blank")
        elif not EMAIL_REGEX.match(postdata['email']):
            errors.append('Invalid email')
        if len(postdata['pwd']) < 1:
            error.append("Password cannot be blank")
        elif len(postdata['pwd']) < 8:
            error.append("Password must be greater than 8 charcacters")
        elif not PWD_REGEX.match(postdata['pwd']):
            errors.append('Password must include one lowercase, one uppercase letter, and a number')
        if len(postdata['confpwd']) < 1:
            error.append("Please confirm password")
        elif postdata['pwd'] != postdata['confpwd']:
            error.append("Passwords do not match!")
        if len(errors)==0:
            hashed = bcrypt.hashpw(postdata['pwd'].encode(), bcrypt.gensalt())
            user = User.objects.create(fname=postdata['fname'], lname=postdata['lname'], email=postdata['email'], password = hashed)
            return (True, user)
        else:
            return (False, errors)
    
    def login_validate(self,postdata):
        errors=[]
        if postdata['email']=="" and postData['pwd']=="":
            errors.append("Fields cannot be left empty")
            return (False, errors)
        if postdata['email']=="":
            errors.append("Email is required")
        elif postdata['pwd']=="":
            errors.append("Password is required")
        elif len(postdata['pwd'])>15:
            errors.append("Password is too long")
        if not User.objects.filter(email=postdata['email']) or not User.objects.filter(password=postdata['pwd']):
            errors.append("Incorrect email or password")
        if len(errors)!=0:
            return (False, errors)
        else:
            user = self.get(email=postdata['email'])
            return (True, user)



class User(models.Model):
    fname = models.CharField(max_length=45)
    lname = models.CharField(max_length=45)
    email = models.CharField(max_length=65)
    password = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
