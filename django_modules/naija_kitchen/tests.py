from django.test import TestCase
from django.urls import reverse

from naija_kitchen.app_models import Restaurant

# Create your tests here.


class RestaurantTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.restaurant = Restaurant.objects.create(
            restaurant_name="A good title",
            restaurant_address="An excellent subtitle",
            restaurant_image="To be set",
            restaurant_contact="test@gmail.com",
        )

    def test_restaurant_content(self):
        self.assertEqual(self.restaurant.restaurant_name, "A good title")
        self.assertEqual(self.restaurant.restaurant_address,
                         "An excellent subtitle")
        self.assertEqual(self.restaurant.restaurant_image, "To be set")
        self.assertEqual(self.restaurant.restaurant_contact, "test@gmail.com")

    def test_restaurant_listview(self):
        response = self.client.get(reverse("Get Restaurant Names"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "An excellent subtitle")
        self.assertTemplateUsed(response, "restaurant_list.html")
