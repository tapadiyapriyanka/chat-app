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
from django.utils.decorators import method_decorator
from .forms import Post_Form
from rest_framework.generics import ListCreateAPIView
from .serializers import SubscriberSerializer


from rest_framework import parsers, renderers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer

from chat_project.authentication import UserAuthentication



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


class chatListView(TemplateView):
	@method_decorator(login_required)
	def get(self, request, *args, **kwargs):
		chat_messages = chatmessage.objects.all()
		total_messages = chat_messages.count()
		form = Post_Form(request.POST or None)
		if request.method == "POST":
			instance = form.save(commit=False)
			instance.username = request.user
			instance.save()
		context = {
			'chat_messages': chat_messages,
			"form" : form,
		}
		return render(request, 'chat_detail.html', context)

	def post(self, request, *args, **kwargs):
		chat_messages = chatmessage.objects.all()
		total_messages = chat_messages.count()
		form = Post_Form(request.POST or None)
		instance = form.save(commit=False)
		instance.username = request.user
		instance.save()
		context = {
			'chat_messages': chat_messages,
			"form" : form,
		}
		return render(request, 'chat_detail.html', context)

		# if request.is_ajax():
		# 	self.template_name = 'chat/delete.html'
		# self.template_name = 'chat_detail.html'
		# return self.render_to_response({'chat_messages': chat_messages, "form" : form})



'''
class SubscriberView(ListCreateAPIView):
	serializer_class = SubscriberSerializer
	queryset = chatmessage.objects.all()

	# def post(self, request):
	#     serializer = SubscriberSerializer(data=request.data)
	#     if serializer.is_valid():
	#         subscriber_instance = Subscriber.objects.create(**serializer.data)
	#     else:
	#         return Response({"errors": serializer.errors})

	# def get(self, request):
	#     all_subscribers = chatmessage.objects.all()
	#     serialized_subscribers = SubscriberSerializer(all_subscribers, many=True)
	#     return Response(serialized_subscribers.data)
'''
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
