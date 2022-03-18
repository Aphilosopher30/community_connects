from django.db import models

# Create your models here.

class Need(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)

    supporters_needed = models.IntegerField(null=True)
    time_frame = models.CharField(max_length=200)

    notes = models.CharField(max_length=1000, null=True)
    adress = models.CharField(max_length=200, null=True)
    contact_info = models.CharField(max_length=200, null=True)

    # status:  (enum. [active, inactive])


    def __str__(self):
        return self.title



class Categories(models.Model):
    tag = models.CharField(max_length=200)

    def __str__(self):
        return self.tag



class NeedCategories(models.Model):
    category = models.ForeignKey(Categories, on_delete = models.CASCADE)
    need = models.ForeignKey(Need, on_delete = models.CASCADE)



# class Supporters(models.Model):
#     name = models.CharField(max_length=200)
#     email = models.CharField(max_length=200)

# class what they signed up for supporters_need

# info on makeing a
# https://hackernoon.com/using-enum-as-model-field-choice-in-django-92d8b97aaa63




#vonuntere for now add paied connection later.
