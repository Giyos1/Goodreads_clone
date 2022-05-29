import time
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from users.forms import UserCreateForm, UserLoginForm


# Create your views here.


class RegisterView(View):
    def get(self, request):
        create_form = UserCreateForm()
        context = {
            "form": create_form
        }
        return render(request, 'users/register.html', context)

    def post(self, request):
        create_form = UserCreateForm(data=request.POST)
        if create_form.is_valid():
            create_form.save()
            return redirect('users:login')

        context = {
            "form": create_form
        }
        return render(request, 'users/register.html', context)


class LoginView(View):
    def get(self, request):
        login_form = UserLoginForm()
        return render(request, 'users/login.html', {'form': login_form})

    def post(self, request):
        login_form = UserLoginForm(data=request.POST)

        if login_form.is_valid():
            """1- agar formada validatsiyalarni qoysa shunday boladi"""
            user = login_form.get_user()
            login(request, user=user)
            return redirect('users:register')
            # 2-usul viewda qisa hammasini shunaqa boladi ln bu yaxshi usul emas
            # cd = login_form.cleaned_data
            # username = cd.get('username')
            # password = cd.get('password')
            # user = authenticate(request, username, password)
            # if user:
            #     if user.is_active:
            #         login(request, user)
            #         return redirect('users:register')
            #     return HttpResponse('User deseblad')
            # return HttpResponse('user unavailable')
        return render(request, 'users/login.html', {'form': login_form})
