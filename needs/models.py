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

    # t.integer "supporters_needed"
    # t.integer "status"
    # t.datetime "created_at", null: false
    # t.datetime "updated_at", null: false
