from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer  # Ensure you have a serializer for Menu

class MenuViewTest(TestCase):
    def setUp(self):
        """Create test instances of the Menu model."""
        self.client = APIClient()  # APIClient is used for API requests
        self.menu1 = Menu.objects.create(title="Pizza", price=9.99, inventory=10)
        self.menu2 = Menu.objects.create(title="Burger", price=5.99, inventory=15)
        self.menu3 = Menu.objects.create(title="Pasta", price=7.99, inventory=20)

    def test_getall(self):
        """Test retrieving all Menu objects via API."""
        response = self.client.get(reverse('menu-list'))  # Ensure this URL name exists
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)  # Serialize the expected data
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # Check HTTP response
        self.assertEqual(response.data, serializer.data)  # Compare response with expected data
