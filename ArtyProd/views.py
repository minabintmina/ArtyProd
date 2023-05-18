from django.shortcuts import render, redirect
from django.contrib import auth

def Portfolio(request):
    return render(request,"Portfolio.html")

def logout(request):
    auth.logout(request)
    return redirect('Portfolio')