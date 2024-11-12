from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from naija_kitchen.models import Restaurant


class APITests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Restaurant.objects.create(
            title="Django for APIs",
            subtitle="Build web APIs with Python and Django",
            author="William S. Vincent",
            isbn="9781735467221",
        )


def test_api_listview(self):
    response = self.client.get(reverse("restaurant_list"))
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(Restaurant.objects.count(), 1)
    self.assertContains(response, self.Restaurant)
