from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .models import Profiles
from . import forms

def signup_view(request):
    if request.method == 'POST':
         form = UserCreationForm(request.POST)
         details = forms.ProfileForm(request.POST)
         if form.is_valid() and details.is_valid():
             user = form.save()
             details.save()
             #  log the user in
             login(request, user)
             return redirect('articles:list')
    else:
        form = UserCreationForm()
        details = forms.ProfileForm()
    return render(request, 'accounts/signup.html', { 'form': form, 'details': details })

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log the user in
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
               return redirect('articles:list')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', { 'form': form })

def logout_view(request):
    if request.method == 'POST':
            logout(request)
            return redirect('articles:list')

def profile_view(request):
    details = Profiles.objects.all()
    etails = Profiles.objects.get(username=request.user)
    return render(request, 'accounts/profile.html', { 'form': etails })