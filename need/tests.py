# from django.test import TestCase
# from need.models import Need
# from need.models import Categories
#
# # Create your tests here.
#
# class TestNeedModel(TestCase):
#     def test_model_str(self):
#         test = Need.objects.create(title = "Django Testing",
#                                     description = "this is a test",
#                                     time_frame = "noon",
#                                     supporters_needed = 5,
#                                     notes = "notes notes notes",
#                                     location = "here",
#                                     contact_info = "phone number or email"
#                                     )
#
#         self.assertEqual(str(test), "Django Testing")
#         self.assertEqual(test.title, "Django Testing")
#         self.assertEqual(test.description, "this is a test")
#         self.assertEqual(test.time_frame, "noon")
#         self.assertEqual(test.supporters_needed, 5)
#         self.assertEqual(test.notes, "notes notes notes")
#         self.assertEqual(test.location, "here")
#         self.assertEqual(test.contact_info, "phone number or email")
#
#
# class TestCategoriesModel(TestCase):
#     def test_model_str(self):
#         tag = Categories.objects.create(tag="tag testing")
#
#         self.assertEqual(str(tag), "tag testing")
