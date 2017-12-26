from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.template.response import TemplateResponse
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . models import chatmessage
from django.contrib.auth.decorators import login_required

# Create your views here.
class homePageView(TemplateView):
    template_name = "base.html"

class chatEditdeleteView(TemplateView):
    template_name = "edit_delete.html"

def logout_method(request):
    return HttpResponse('You Logged out successfully..')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()

    response = TemplateResponse(request, 'registration/signup.html', {'form': form})
    return response
    # template_name = 'registation/signup.html'
    # return template_name
    # #return render(request, 'registation/signup.html', {'form' : form})
@login_required
def chatListView(request):
    return render(request, 'home.html', {'model':chatmessage})
    # model = chatmessage
    # template_name = 'home.html'

class chatDetailView(DetailView):
    model = chatmessage
    template_name = 'chat_detail.html'
    context_object_name = 'anything_you_want'

# class chatCreateView(CreateView):
#     model = chatmessage
#     template_name = 'chat_new.html'
#     fields = '__all__'

class chatUpdateView(UpdateView):
    model = chatmessage
    template_name = 'chat_edit.html'
    fields = ['textmsg']

class chatDeleteView(DeleteView):
    model = chatmessage
    template_name = 'chat_delete.html'
    success_url = reverse_lazy('homepage')