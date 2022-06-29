import graphene
from graphene_django import DjangoObjectType
from .models import Need, Categories, Supporters


############

class NeedsType(DjangoObjectType):
    class Meta:
        model = Need
        fields = ("id", "title", "description", "supporters_needed", "time_frame", "notes", "location", "contact_info")

class NeedsMutation(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)

    need = graphene.Field(NeedsType)

    @classmethod
    def mutate(cls, root, info, title): # reserch what root and info are for
        need = Need(title=title)
        need.save()

        return NeedsMutation(need=need)

############

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

        category.save()

        return CategoriesMutation(category=category)

############

class SupportersType(DjangoObjectType):
    class Meta:
        model = Supporters
        fields = ("id", "first_name", "last_name", "address", "email", "phone", "phone_text")

class SupportersMutation(graphene.Mutation):

    class Arguments:
        email  = graphene.String(required=True)
        first_name  = graphene.String(required=True)
        last_name = graphene.String(required=True)
        address = graphene.String(required=True)
        phone = graphene.String(required=False)
        phone_text = graphene.String(required=False)

    supporter = graphene.Field(SupportersType)

    @classmethod
    def mutate(cls, root, info, first_name, last_name, email, address, phone, phone_text): # reserch what root and info are for
        supporter = Supporters(first_name=first_name, last_name=last_name, email=email, address=address, phone=phone, phone_text=phone_text)
        supporter.save()
        return SupportersMutation(supporter=supporter)

############

#need_catagories

############

#supporters_catagories



class Mutation(graphene.ObjectType):
    add_need = NeedsMutation.Field()
    add_category = CategoriesMutation.Field()
    add_supporter = SupportersMutation.Field()

class Query(graphene.ObjectType):

    all_needs = graphene.List(NeedsType)
    def resolve_all_needs(root, info):
        return Need.objects.all()

    get_need = graphene.Field(NeedsType, id=graphene.Int())
    def resolve_get_need(root, info, id):
        return Need.objects.get(pk=id)

    all_supporters = graphene.List(SupportersType)
    def resolve_all_supporters(root, info):
        return Supporters.objects.all()



schema = graphene.Schema(query=Query, mutation = Mutation)
# schema = graphene.Schema(query=Query)


# needs have persons
# persons have catagories they volunire for (many to many)
# name, contact_info (phone_text, phone, email, adress,) date_created_time_stamp, last_modified_time_stamp


# people
# need by id: or other search mechanism
# frontend
# lader: administrater privilages
# later: delete
# later: editing -
