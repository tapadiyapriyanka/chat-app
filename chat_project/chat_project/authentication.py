import jwt

from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from rest_framework import exceptions
from rest_framework.authentication import TokenAuthentication
from rest_framework.authentication import (
    BaseAuthentication,
    get_authorization_header
)
# class JSONWebTokenAuthentication(TokenAuthentication):
#     def authenticate_credentials(self, key):
#         try:
#             payload = jwt.decode(key, settings.SECRET_KEY)
#             user = User.objects.get(username=payload['username'])
#         except (jwt.DecodeError, User.DoesNotExist):
#             raise exceptions.AuthenticationFailed('Invalid token')
#         except jwt.ExpiredSignatureError:
#             raise exceptions.AuthenticationFailed('Token has expired')
#         if not user.is_active:
#             raise exceptions.AuthenticationFailed('User inactive or deleted')
#         return (user, payload)



def authenticate(self, request):
    auth = get_authorization_header(request).split()

    if not auth or auth[0].lower() != b'token':
        return None
    if len(auth) == 1:
        msg = _('Invalid token header. No credentials provided.')
        raise exceptions.AuthenticationFailed(msg)
    elif len(auth) > 2:
        msg = _('Invalid token header. '
                'Token string should not contain spaces.')
        raise exceptions.AuthenticationFailed(msg)

    user, auth_token = authenticate_credentials(auth[1])
    return (user, auth_token)


def authenticate_credentials(self, token):
    '''
    Due to the random nature of hashing a salted value, this must inspect
    each auth_token individually to find the correct one.
    Tokens that have expired will be deleted and skipped
    '''
    msg = _('Invalid token.')
    token = token.decode("utf-8")
    for auth_token in AuthToken.objects.filter(
            token_key=token[:CONSTANTS.TOKEN_KEY_LENGTH]):
        for other_token in auth_token.user.auth_token_set.all():
            if other_token.digest != auth_token.digest and other_token.expires is not None:
                if other_token.expires < timezone.now():
                    other_token.delete()
        if auth_token.expires is not None:
            if auth_token.expires < timezone.now():
                auth_token.delete()
                continue
        try:
            digest = hash_token(token, auth_token.salt)
        except TypeError:
            raise exceptions.AuthenticationFailed(msg)
        if digest == auth_token.digest:
            return validate_user(auth_token)
    # Authentication with this token has failed
    raise exceptions.AuthenticationFailed(msg)

def validate_user(self, auth_token):
    if not auth_token.user.is_active:
        raise exceptions.AuthenticationFailed(
            _('User inactive or deleted.'))
    return (auth_token.user, auth_token)

def authenticate_header(self, request):
    return 'Token'
