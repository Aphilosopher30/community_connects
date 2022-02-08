from django.test import TestCase
from needs.models import Need


# Create your tests here.

class TestNeedModel(TestCase):
    def test_model_str(self):
        title = Need.objects.create(title="Django Testing")
        self.assertEqual(str(title), "Django Testing")
