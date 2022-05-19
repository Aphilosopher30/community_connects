
from django.urls import path
from graphene_django.views import GraphQLView
from need.schema import schema
from . import views

urlpatterns = [
    path('graphql', GraphQLView.as_view(graphiql=True, schema=schema)),
    path("hello/", views.say_hello)
]
