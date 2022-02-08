from django.db import models

# Create your models here.

class Need(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    start_time = models.CharField(max_length=200)
    end_time = models.CharField(max_length=200)

    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=200)

    supporters_needed = models.IntegerField(null=True)
    # supporters_needed = models.IntegerField(null=True)

    def __str__(self):
        return self.title



class Categories(models.Model):
    tag = models.CharField(max_length=200)

    def __str__(self):
        return self.tag



class NeedCategories(models.Model):
    category = models.ForeignKey( Categories, on_delete = models.CASCADE)
    need = models.ForeignKey( Need, on_delete = models.CASCADE)



# class Supporters(models.Model):
#     name = models.CharField(max_length=200)
#     email = models.CharField(max_length=200)
# info on makeing a
# https://hackernoon.com/using-enum-as-model-field-choice-in-django-92d8b97aaa63
