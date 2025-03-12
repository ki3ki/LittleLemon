from django.test import TestCase
from restaurant.models import Menu  # Adjust the import based on your app structure

class MenuTest(TestCase):
    def test_menu_str_representation(self):
        # Create a new Menu instance
        menu_item = Menu.objects.create(title="Pasta", price=12.99, inventory=10)
        
        # Assert that the string representation matches the expected output
        expected_output = "Pasta : 12.99"
        self.assertEqual(str(menu_item), expected_output)
