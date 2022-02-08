from django.test import TestCase
from needs.models import Need
from needs.models import Categories


# Create your tests here.

class TestNeedModel(TestCase):
    def test_model_str(self):
        title = Need.objects.create(title="Django Testing")
        self.assertEqual(str(title), "Django Testing")


class TestCategoriesModel(TestCase):
    def test_model_str(self):
        tag = Categories.objects.create(tag="Django Testing")
        self.assertEqual(str(title), "Django Testing")
