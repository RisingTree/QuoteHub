from django.db import models
import re
import bcrypt
class UserManager(models.Manager):
    def registration_validator(self,postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name should be atleast 2 characters"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name should be atleast 2 characters"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = ('Invalid email address')
        if len(postData['password']) < 8:
            errors['password'] = "Pasword should be atleast 8 characters"
        if postData['confirm_password'] != postData['password']:
            errors['confirm_password'] = 'Passwords must match'
        return errors
    def login_validator(self,postData):
        errors = {}
        user_email = User.objects.filter(email=postData['log_match'])
        if not user_email:
            errors['log_match'] = 'Incorrect email'
        elif  not bcrypt.checkpw(postData['pass_match'].encode(), user_email[0].password.encode()):
            errors['pass_match'] = 'Incorrect Password'
        return errors
    def edit_validator(self, postData):
        errors={}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['update_email']):
            errors['update_email'] = 'Invalid email address'
        if len(postData['update_first']) < 2:
            errors['update_first'] = "First name should be atleast 2 characters"
        if len(postData['update_last']) < 2:
            errors['update_last'] = "Last name should be atleast 2 characters"
        if User.objects.filter(email = postData['update_email']):
            errors['same_email'] = "Email already registered, try again"
        return errors
        
class User(models.Model):
    first = models.CharField(max_length=255)
    last = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    objects= UserManager()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now =True)

class QuoteManager(models.Manager):
    def quote_validator(self,postData):
        errors={}
        if len(postData['quote']) < 10:
            errors['quote'] = 'More than 10 characters'
        if len(postData['author']) <3 :
            errors['author'] = 'More than 3 characters'
        return errors
class Quotes(models.Model):
    quote = models.CharField(max_length=255)
    author= models.CharField(max_length=255)
    created_by= models.ForeignKey(User, related_name='qoutes')
    liked_by = models.ManyToManyField(User, related_name="quotes_liked")
    objects= QuoteManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

