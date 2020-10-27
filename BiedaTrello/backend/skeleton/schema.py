from graphene_django import DjangoObjectType
import graphene
from .models import UserModel

# this file is something like top-level urls.py
# where we define our "endpoints"
class UserType(DjangoObjectType):
    class Meta:
        model = UserModel
        fields = ("name", "last_name")

class Query(graphene.ObjectType):
    users = graphene.List(UserType)

    def resolve_users(self, info):
        return UserModel.objects.all()

schema = graphene.Schema(query=Query)