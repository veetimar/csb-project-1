from django.urls import path

from .views import index, register, message, user

urlpatterns = [
    path("", index, name="index"),
    path("register/", register, name="register"),
    path("message/", message, name="message"),
    path("user/<str:username>", user, name="user")  # remove '<str:username>'
]
