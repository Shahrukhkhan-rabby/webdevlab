import jwt
from django.conf import settings
from .models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpRequest
from typing import Optional
from graphql import GraphQLError


def get_user_from_token(request: HttpRequest) -> Optional[User]:
    token = request.META.get('HTTP_AUTHORIZATION', None)
    if token and token.startswith('Bearer '):
        token = token.split(' ')[1]
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            user_id = payload['user_id']
            user = User.objects.get(pk=user_id)
            if not user.is_active:
                raise GraphQLError("User is not active")
            return user
        except (jwt.ExpiredSignatureError, jwt.InvalidTokenError, ObjectDoesNotExist) as e:
            return e