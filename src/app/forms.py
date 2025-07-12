from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(label="Username", required=True, max_length=20)
    password = forms.CharField(label="Password", required=True, widget=forms.PasswordInput())
