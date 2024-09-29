from django.views import View
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

from .forms import UserRegistrationForm

# Create your views here.
class LoginView(View):
    template_name = 'users/login.html'

    def get(self, request: HttpRequest):
        form = AuthenticationForm()
        data = {'form': form}
        return render(request, self.template_name, data)
    
    def post(self, request: HttpRequest):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
        data = {'form': form}
        return render(request, self.template_name, data)

class SignUpView(View):
    template_name = 'users/signup.html'

    def get(self, request: HttpRequest):
        form = UserRegistrationForm()
        data = {'form': form}
        return render(request, self.template_name, data)
    
    def post(self, request: HttpRequest):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        data = {'form': form}
        return render(request, self.template_name, data)