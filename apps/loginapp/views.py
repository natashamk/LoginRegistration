from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
# Create your views here.

def index(request):
    if not 'id' in request.session:
        request.session['id'] = None
    if request.session['id'] != None:
        return redirect ('/success')
    else:
        return render(request, 'loginapp/index.html')

def process(request):
    result = User.objects.basic_validate(request.POST)
    if result[0]:
        request.session['id'] = result[1].id;
        return redirect('/success')
    else:
        for error in result[1]:
            messages.error(request, error)
        return redirect('/success')

def loginprocess(request):
    result = User.objects.login_validate(request.POST)
    if result[0]:
        request.session['id'] = result[1].id
        return redirect('/success')
    else:
        for error in result[1]:
            messages.error(request, error)
        return redirect('/')

def success(request):
    if request.session['id'] == None:
        messages.error(request,"You are not logged in")
        return redirect ('/')
    else:
        return render(request, 'loginapp/success.html')
    
def logout(request):
    request.session.clear()
    return redirect('/')