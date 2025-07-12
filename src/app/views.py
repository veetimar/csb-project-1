from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden
from django.core.exceptions import ValidationError
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

from .forms import RegisterForm, MessageForm
from .models import Account, Message

def index(request):
    if request.method == "GET":
        messages = Message.objects.all()
        return render(request, "app/index.html", {"messages": messages})

@login_required
@csrf_exempt  # remove this line
def message(request):
    if request.method == "GET":
        return render(request, "app/message.html", {"form": MessageForm})
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            owner = Account.objects.get(user=request.user)
            if owner.balance <= 0:
                return HttpResponseForbidden("You have run out of messages")
            owner.balance -= 1
            owner.save()
            content = request.POST.get("content")
            new_message = Message(owner=owner, content=content)
            new_message.save()
            return redirect("/")
        else:
            return HttpResponseForbidden("Form data not valid")

def register(request):
    if request.method == "GET":
        return render(request, "app/register.html", {"form": RegisterForm})
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")
            # try:
            #     validate_password(password=password)
            # except ValidationError as e:
            #     return HttpResponseForbidden(e)
            user = User.objects.create_user(username=username, password=password)
            account = Account(user=user)
            account.save()
            login(request, user)
            return redirect("/")
        else:
            return HttpResponseForbidden("Form data not valid")

def user(request, username):  # remove the username parameter
    account = Account.objects.get(user__username=username)  # replace with '.get(user=request.user)'
    return render(request, "app/user.html", {"account": account})
