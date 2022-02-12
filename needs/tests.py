from django.test import TestCase
from needs.models import Need
from needs.models import Categories


# Create your tests here.

class TestNeedModel(TestCase):
    def test_model_str(self):
        test = Need.objects.create(title="Django Testing",
                                    description="this is a test",
                                    start_time="noon",
                                    supporters_needed = 5
                                    )

        self.assertEqual(str(test), "Django Testing")
        self.assertEqual(test.title, "Django Testing")
        self.assertEqual(test.description, "this is a test")
        self.assertEqual(test.start_time, "noon")
        self.assertEqual(test.supporters_needed, 5)


class TestCategoriesModel(TestCase):
    def test_model_str(self):
        tag = Categories.objects.create(tag="tag testing")
        self.assertEqual(str(tag), "tag testing")
