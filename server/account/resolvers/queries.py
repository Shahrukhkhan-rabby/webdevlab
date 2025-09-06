import graphene
from account.utils import get_user_from_token
from graphql import GraphQLError
from .queryTypes import GetUserType
from ..models import User


class Query(graphene.ObjectType):
    users = graphene.List(GetUserType)
    user_by_id = graphene.Field(GetUserType, id=graphene.String())
    protected_auth = graphene.Field(GetUserType)

    def resolve_users(root, info, **kwargs):
        return User.objects.all()

    def resolve_user_by_id(root, info, id):
        return User.objects.get(pk=id)

    def resolve_protected_auth(root, info):
        user = get_user_from_token(info.context)
        if not user:
            raise GraphQLError("Authentication failed: User not found")
        return user