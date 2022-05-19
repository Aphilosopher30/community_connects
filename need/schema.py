import graphene
from graphene_django import DjangoObjectType
from .models import Need, Categories


class NeedsType(DjangoObjectType):
    class Meta:
        model = Need
        fields = ("id", "title", "description", "supporters_needed", "time_frame", "notes", "location", "contact_info")


class Query(graphene.ObjectType):
    all_needs = graphene.List(NeedsType)


class NeedsMutation(graphene.Mutation):

    class Arguments:
        title = graphene.String(required=True)

    need = graphene.Field(NeedsType)

    @classmethod
    def mutate(cls, root, info, title): # reserch what root and info are for
        need = Need(title=title)
        # breakpoint()
        need.save()

        return NeedsMutation(need=need)





class CategoriesType(DjangoObjectType):
    class Meta:
        model = Categories
        fields = ("id", "tag")

class CategoriesMutation(graphene.Mutation):

    class Arguments:
        tag = graphene.String(required=True)

    category = graphene.Field(CategoriesType)

    @classmethod
    def mutate(cls, root, info, tag): # reserch what root and info are for
        category = Categories(tag=tag)
#         # breakpoint()

        category.save()

        return CategoriesMutation(category=category)



class Mutation(graphene.ObjectType):
    add_need = NeedsMutation.Field()
    add_category = CategoriesMutation.Field()

    # breakpoint()



schema = graphene.Schema(query=Query, mutation = Mutation)
