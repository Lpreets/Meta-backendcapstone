from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from restaurant.models import Menu

class MenuViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a few menu items for testing
        Menu.objects.create(Name="Dish 1", No_of_guests=4, BookingDate="2023-04-15")
        Menu.objects.create(Name="Dish 2", No_of_guests=2, BookingDate="2023-04-16")
        Menu.objects.create(Name="Dish 3", No_of_guests=6, BookingDate="2023-04-17")

    def setUp(self):
        self.client = APIClient()

    def test_getall(self):
        response = self.client.get(reverse('menu'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 3)
