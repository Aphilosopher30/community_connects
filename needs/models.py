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
    supporters_needed = models.IntegerField(null=True)

    # def __str__(self):
    #     return self.title

class Need(models.Model):
