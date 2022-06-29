from django.db import models

# Create your models here.

class Need(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)

    supporters_needed = models.IntegerField(null=True)
    time_frame = models.CharField(max_length=200)

    notes = models.CharField(max_length=1000, null=True)
    location = models.CharField(max_length=200, null=True)
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


class Supporters(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=1000)

    email = models.CharField(max_length=200)
    address = models.CharField(max_length=200, null=True)

    phone = models.CharField(max_length=2000, null=True)
    phone_text = models.CharField(max_length=200, null=True)

    # supporter_categories = models.ForeignKey(Need, on_delete = models.CASCADE)

    def __str__(self):
        return self.last_name



class SupportersCategories(models.Model):
    category = models.ForeignKey(Categories, on_delete = models.CASCADE)
    supporter = models.ForeignKey(Supporters, on_delete = models.CASCADE)




# info on makeing a
# https://hackernoon.com/using-enum-as-model-field-choice-in-django-92d8b97aaa63


#vonuntere for now add paied connection later.
