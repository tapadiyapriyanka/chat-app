import datetime
import jwt

from django.conf import settings
from django.shortcuts import render_to_response, redirect, get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.template import RequestContext

from django.contrib.auth import authenticate
from rest_framework import parsers, renderers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer

from .authentication import UserAuthentication

from django.db import transaction
from .authentication import UserSerializer, UserLoginSerializer

class JSONWebTokenAuth(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = AuthTokenSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            # print('test',serializer['username'])
            user = serializer.validated_data['user']
            token = jwt.encode({
                'username': user.username,
                'iat': datetime.datetime.utcnow(),
                'nbf': datetime.datetime.utcnow() + datetime.timedelta(minutes=-5),
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7)
            }, settings.SECRET_KEY)
            return Response({'success':True, 'message':'Successfully logged in', 'data': { 'token': token}})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

json_web_token_auth = JSONWebTokenAuth.as_view()


class RegistrationView(APIView):
    """
    View for registering a new user to your system.
    **Example requests**:
        POST /api/auth/register/
    """

    @transaction.atomic()
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    """
    View for login a user to your system.
    **Example requests**:
        POST /api/auth/login/
    """

    def post(self, request):
        username = request.data.get('username', None)
        password = request.data.get('password', None)
        authenticated_user = authenticate(username=username, password=password)
        if authenticated_user:
            serializer = UserLoginSerializer(authenticated_user)
            return render_to_response('base.html',{"user":request.user})
                              # context_instance=RequestContext(request))
            # response = redirect('home')
            # response['Token'] = serializer.data
            # response = HttpResponseRedirect(reverse('home'))
            # request.session['username'] = serializer.data
            # response['HTTP_AUTHORIZATION'] = 'Basic realm="%s"' % serializer.data
            # return response
            # return redirect('home')
            # Response(serializer.data, status=status.HTTP_200_OK)
            # return Response['Location'] = serializer.get_absolute_url()
        return Response("Invalid Credentials", status=status.HTTP_401_UNAUTHORIZED)
