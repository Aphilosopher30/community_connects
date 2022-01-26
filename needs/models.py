from django.db import models

# Create your models here.

class Need(models.Model):
    title = models.CharField()
    description = models.CharField()
    start_time = models.CharField()
    end_time = models.CharField()

    city = models.CharField()
    state = models.CharField()
    zip_code = models.CharField()
    street_address = models.CharField()
    street_address = models.CharField()
    street_address = models.CharField()
    # t.integer "supporters_needed"
    # t.integer "status"
    # t.datetime "created_at", null: false
    # t.datetime "updated_at", null: false
