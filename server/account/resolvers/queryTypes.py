from account.models import User
from graphene_django.types import DjangoObjectType
import graphene

class UserType(DjangoObjectType):
    class Meta:
        model = User
class GetUserType(DjangoObjectType):
    class Meta:
        model = User
        exclude = ("password",)