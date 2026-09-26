from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from accounts.models import User
from .models import Category, Product, ProductVariant

class CategoryTreeTests(APITestCase):
    def test_nested_categories_appear_in_tree(self):
        root = Category.objects.create(name="Electronics")
        child = Category.objects.create(name="Arduino", parent=root)
        response = self.client.get("/api/categories/tree/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        admin = User.objects.create_user(username="a", password="x", role=User.Role.ADMIN)
        self.client.force_authenticate(admin)
        response = self.client.get("/api/categories/tree/")
        self.assertEqual(response.data[0]["name"],"Electronics")
        self.assertEqual(response.data[0]["children"][0]["name"], "Arduino")

class RolePermisionTests(APITestCase):
    def setUp(self):
        self.viewer = User.objects.create_user(username="v", password="x", role=User.Role.VIEWER)
        self.inventory = User.objects.create_user(username="i", password="x", role=User.Role.INVENTORY)

    def test_if_viewr_can_read_prodx(self):
        self.client.force_authenticate(self.viewer)
        self.assertEqual(self.client.get("/api/products/").status_code, status.HTTP_200_OK)

    def test_if_viewr_cannt_create_prodx(self):
        self.client.force_authenticate(self.viewer)
        response = self.client.post("/api/products/", {"name": "New"})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_inventory_role_can_create_prodx(self):
        self.client.force_authenticate(self.inventory)
        response = self.client.post("/api/products/", {"name": "New"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class VariantSerializerTests(APITestCase):
    def test_variant_show_stock_quantity(self):
        admin = User.objects.create_user(username="a2", password="x", role=User.Role.ADMIN)
        self.client.force_authenticate(admin)
        product = Product.objects.create(name="Widget")
        variant = ProductVariant.objects.create(product=product, price=10)

        response = self.client.get(f"/api/variants/{variant.id}/")
        self.assertIn("quantity", response.data)
        self.assertEqual(response.data["quantity"],0)

