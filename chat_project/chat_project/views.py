import datetime
import jwt

from django.conf import settings

from rest_framework import parsers, renderers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer

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
