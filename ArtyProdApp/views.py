from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project, Services, Team, SignUp, Contact, Personnel
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib import auth
from .forms import ContactForm, ProjectForm
import sys

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            text = form.cleaned_data['text']
            contact = Contact(subject=subject, text=text)
            form.instance.sender_username = request.user.username
            form.save()
            contact.save()
            messages.info(request, 'Thank You For Your Submition')
            return redirect('Portfolio')
    else:
        form = ContactForm()
    return render(request, 'Contact.html', {'form': form})

def project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            form.instance.sender_username = request.user.username
            form.save()
            project.save()
            return redirect('Portfolio')
    else:
        form = ProjectForm()
    context = {'form': form}
    return render(request, 'Project.html', context)

def projects(request):
    projects = Project.objects.all()
    return render(request, 'Projects.html', {'projects': projects})

def portfolio(request):
    return HttpResponse('portfolio.html')
        
def service(request):
    services = Services.objects.all()
    return render(request, 'Services.html', {'services': services})

def personnel(request):
    personnels = Personnel.objects.all()
    return render(request, 'Team.html', {'personnels': personnels})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('Portfolio')
        else:
            messages.info(request, 'Invalid Username or Password')
            return redirect('Login')
    else:
        return render(request, 'Login.html')

def signup(request):
    User = get_user_model()
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username is already taken')
                return redirect(signup)
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email is already taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                user.save()
                return redirect('Login')
        else:
            messages.info(request, 'Both passwords are not matching')
            return redirect(signup)
    else:
        return render(request, 'SignUp.html')
# Create your views here.

def Myproject(request):
    projects = Project.objects.all()
    return render(request, 'MyProjects.html', {'projects': projects})