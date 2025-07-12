from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(label="Username", required=True, max_length=20)
    password = forms.CharField(label="Password", required=True, widget=forms.PasswordInput())

class MessageForm(forms.Form):
    content = forms.CharField(label="New message", required=True, max_length=100)
