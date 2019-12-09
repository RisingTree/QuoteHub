from django.shortcuts import render,redirect
from .models import User, Quotes
from django.contrib import messages
import bcrypt

def login_registration(request):
    return render(request, 'dash_app/login.html')
def register(request):
    errors = User.objects.registration_validator(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request,value, extra_tags=key)
        return redirect('/')
    else:
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    user = User.objects.create(first=request.POST['first_name'],last=request.POST['last_name'] , email= request.POST['email'],password= pw_hash ) 
    request.session['userid'] = user.id
    return redirect('/quotes')
def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request,value, extra_tags=key)
        return redirect('/')
    else:
        user = User.objects.get(email=request.POST['log_match'])
        request.session['userid']= user.id
        return redirect('/quotes')
def dashboard(request):
    if 'userid' not in request.session:
        return redirect('/')
    context = {
        'user': User.objects.get(id=request.session['userid']),
        'all_quotes':Quotes.objects.all,
    }
    return render(request, 'dash_app/dashboard.html', context)
def process_quote(request):
    errors=Quotes.objects.quote_validator(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value , extra_tags=key)
        return redirect('/quotes')
    else:
        Quotes.objects.create(quote=request.POST['quote'], author = request.POST['author'],created_by= User.objects.get(id =request.session['userid']))
        return redirect('/quotes')
def user_info (request,id):
    this_user = User.objects.get(id = int(id))
    context={
        'user': User.objects.get(id = int(id)),
        'user_quotes': Quotes.objects.filter(created_by=this_user)
    }
    return render(request, 'dash_app/user_info.html', context)
def delete(request,id):
    delete_quote= Quotes.objects.get(id= int(id))
    delete_quote.delete()
    return redirect('/quotes')
def edit_user(request,id):
    context={
        'user':User.objects.get(id= int(id))
    }
    return render(request, 'dash_app/edit_user.html', context)
def process_edit_account(request, id):
    errors = User.objects.edit_validator(request.POST)
    if len(errors)>0:
        for key,value in errors.items():
            messages.error(request,value, extra_tags=key)
        return redirect(f'/myaccount/{id}')
    else:
        user_update=User.objects.get(id = int(id))
        user_update.first= request.POST['update_first']
        user_update.last= request.POST['update_last']
        user_update.email= request.POST['update_email']
        user_update.save()
        return redirect('/quotes')
def logout(request):
    if 'userid' in request.session:
        del request.session['userid']
    return redirect('/')
def liked_by(request,id):
    liked =User.objects.get(id = request.session['userid'])
    quote_liked = Quotes.objects.get(id=int(id))
    quote_liked.liked_by.add(liked)
    return redirect('/quotes')