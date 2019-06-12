from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from authentification.models import Token
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

import string
import random

def generateToken():
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(21))

class Account(View):

    template = "auth/account.html"

    def get(self, request):
        if request.user.is_authenticated is False:
            return redirect("signin")
        token = Token.objects.get(user=request.user)
        return render(request, self.template, {"token": token.token})


class Signin(View):

    template = "auth/signin.html"

    def get(self, request):
        if request.user.is_authenticated:
            return redirect("account")
        return render(request, self.template)

    def post(self, request):
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse("ok")
        else:
            return HttpResponse("Invalid username / password")

class Signup(View):

    template = "auth/signup.html"

    def get(self, request):
        if request.user.is_authenticated:
            return redirect("account")
        return render(request, self.template)

    def post(self, request):
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        lastName = request.POST.get("lastName", None)
        firstName = request.POST.get("firstName", None)
        email = request.POST.get("email", None)

        if lastName is None or firstName is None:
            return HttpResponse("Last name and First name cannot be empty.")
        if username is None or password is None or email is None:
            return HttpResponse("Error, verify all the fields please.")
        try:
            user = User.objects.get(username=username)
            return HttpResponse("Username already exist!")
        except:
            pass
        try:
            user = User.objects.get(email=email)
            return HttpResponse("Email already used!")
        except:
            pass
        user = User.objects.create_user(username, email, password)
        user.first_name = firstName
        user.last_name = lastName
        user.save()
        token = Token()
        token.user = user
        token.token = generateToken()
        token.save()
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse("ok")
        else:
            return HttpResponse("Failed to log in.")

class Signout(View):

    def get(self, request):
        logout(request)
        return redirect("/")
