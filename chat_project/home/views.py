from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
class HomePage(TemplateView):
    def get(self, request, *args, **kwargs):
        # if request.user.is_authenticated:
        #     return redirect(reverse('chat:chat_home'))
        self.template_name = 'base.html'
        return self.render_to_response({'app': 'app'})

class Login(TemplateView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse('chat:chat_home'))
        self.template_name = 'registration/login.html'
        return self.render_to_response({'app': 'app'})

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username', '')
        pword = request.POST.get('password', '')
        response = {'notes': {'global': []}, 'username': username}
        self.template_name = 'registration/login.html'
        if not username:
            response['notes']['global'].append('Username cannot be empty')
        if not pword:
            response['notes']['global'].append('Password cannot be empty')
        if response['notes']['global']:
            return self.render_to_response({'response': response})
        user = authenticate(username=username, password=pword)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(reverse('chat:chat_home'))
            else:
                response['notes']['global'].append(enGB.invalid_credentials)
        response['notes']['global'].append('Invalid username & password')
        return self.render_to_response({'response': response})


class Logout(TemplateView):
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('/')