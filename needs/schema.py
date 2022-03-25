import graphene
from graphene_django import DjangoObjectType
from .models import Books

class NeedsTypes(DjangoObjectType):
    class Meta:
        model = Need
        fields = ("id", "title", "description", "supporters_needed", "time_frame", "notes", "location", "contact_info")


class Query(graphene.ObjectType):
    all_needs = graphene.List(NeedsType)

schema = graphene.Schema(query=Query)
