from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Feature

# Create your views here.
def index(request):
    feature1 = Feature()
    feature1.id = 0
    feature1.name = 'Feature 1'
    feature1.details = 'This is the first feature'
    return render(request, 'index.html', )

def counter(request):
    links = [1,2,3,4,'John','Peter']
    return render(request, 'counter.html', {'links': links})
   

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
    
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already taken')
                return redirect('register') 
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.success(request, 'Registration successful!')
                return redirect('login')
        else:
            messages.info(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request,'register.html')
    # return render(request, 'register.html')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username , password=password)

        if user is not None:
            auth.login(request , user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')
        
    else:
        return render(request, 'login.html')
  
def logout(request):
    auth.logout(request)
    return redirect('login')

def post(request,pk):
    return render(request, 'post.html', {'pk': pk})