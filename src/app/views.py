from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden
from django.core.exceptions import ValidationError
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

from . import forms
from . import models

def index(request):
    if request.method == "GET":
        return render(request, "app/index.html")

def register(request):
    if request.method == "GET":
        return render(request, "app/register.html", context={"form": forms.RegisterForm})
    if request.method == "POST":
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")
            # try:
            #     validate_password(password=password)
            # except ValidationError as e:
            #     return HttpResponseForbidden(e)
            user = User.objects.create_user(username=username, password=password)
            account = models.Account(user=user)
            account.save()
            login(request, user)
            return redirect("/")
        else:
            return HttpResponseForbidden("Form data not valid")
