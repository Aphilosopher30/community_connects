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

class Categories(models.Model):
    tag = models.CharField(max_length=200)

class NeedCategories(models.Model):
    category = models.ForeignKey( Categories, on_delete = models.CASCADE)
    need = models.ForeignKey( Need, on_delete = models.CASCADE)



#   create_table "supporters", force: :cascade do |t|
#     t.string "name"
#     t.string "email"
#     t.bigint "need_id"
#     t.datetime "created_at", null: false
#     t.datetime "updated_at", null: false
#     t.index ["need_id"], name: "index_supporters_on_need_id"
#   end
#
