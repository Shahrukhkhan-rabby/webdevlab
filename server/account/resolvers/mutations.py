import os
import jwt
import graphene
from .queryTypes import UserType
from account.models import User
from datetime import datetime
from account.EmailSender import EmailSender
from django.conf import settings
from django.contrib.auth import authenticate
from django.utils import timezone


class RegisterUser(graphene.Mutation):

    user = graphene.Field(UserType)

    class Arguments:
        email = graphene.String(required=True)
        password = graphene.String(required=True)
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        birth = graphene.String()

    def mutate(self, info, email, password, first_name, last_name, birth = None):
        birthdate = None
        if birth:
            # Parse the birthdate string into a datetime object
            birthdate = datetime.fromisoformat(birth.replace('Z', '+00:00'))

        # Create the user object
        user = User(
            email=email,
            birth=birthdate,  # Replace 'birthdate' with the actual field in your model
            is_active=False,
            username=email,  # Set username directly
            first_name=first_name,
            last_name=last_name,
        )

        # Set the password
        user.set_password(password)

        # Save the user
        user.save()

        # Generating token
        token_payload = {
            'user_id': user.id,
            'exp': datetime.now() + settings.JWT_EXPIRATION_DELTA
        }
        token = jwt.encode(token_payload, settings.SECRET_KEY, algorithm='HS256').decode('utf-8')

        # Constructing activation link
        activation_link = f"{os.getenv('FRONTEND_URL')}/activate-account/?token={token}"

        # Send email with token for email validation
        email_sender = EmailSender()
        email_sender.send_activation_email(user=user, activation_link=activation_link)

        return RegisterUser(user=user)


class VerifyUser(graphene.Mutation):
    class Arguments:
        token = graphene.String(required=True)

    success = graphene.Boolean()

    @staticmethod
    def mutate(self, info, token):
        try:
            decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            user_id = decoded_token['user_id']
            user = User.objects.get(pk=user_id)
            user.is_active = True
            user.save()
            return VerifyUser(success=True)
        except jwt.ExpiredSignatureError:
            # Handle token expiration
            return VerifyUser(success=False)
        except jwt.InvalidTokenError:
            # Handle invalid token
            return VerifyUser(success=False)


class LoginMutation(graphene.Mutation):
    user = graphene.Field(UserType)
    access_token = graphene.String()
    refresh_token = graphene.String()

    class Arguments:
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    @staticmethod
    def mutate(root, info, email, password):
        user = authenticate(info.context, username=email, password=password)

        if user is None:
            raise Exception("Invalid credentials")

        # Generate access token
        access_payload = {
            'user_id': user.id,
            'exp': timezone.now() + settings.JWT_ACCESS_TOKEN_EXPIRATION_DELTA
        }
        access_token = jwt.encode(access_payload, settings.SECRET_KEY, algorithm='HS256')

        # Generate refresh token
        refresh_payload = {
            'user_id': user.id,
            'exp': timezone.now() + settings.JWT_REFRESH_TOKEN_EXPIRATION_DELTA
        }
        refresh_token = jwt.encode(refresh_payload, settings.SECRET_KEY, algorithm='HS256')

        return LoginMutation(user=user, access_token=access_token.decode(), refresh_token=refresh_token.decode())


class Mutation(graphene.ObjectType):
    register_user = RegisterUser.Field()
    verify_user = VerifyUser.Field()
    login = LoginMutation.Field()