from django.urls import path

from .views import index, register, message

urlpatterns = [
    path("", index, name="index"),
    path("register/", register, name="register"),
    path("message/", message, name="message"),
]
