from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from accounts.models import User
from catalog.models import ProductVariant, Product
from .models import Stock, StockMovement
from .services import apply_movement,InsufficientStockError

class StockServiceTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="k", password="x")
        product = Product.objects.create(name="Resistor")
        self.variant = ProductVariant.objects.create(product=product, price=1)

    def test_receiving_stock_increasment_quntity_and_logz_it(self):
        movment = apply_movement(
            variant=self.variant, delta=20,
            movement_type=StockMovement.Type.IN, reason=StockMovement.Reason.RECEIPT,
            user=self.user,
        )
        self.assertEqual(movment.balance_after, 20)
        self.assertEqual(Stock.objects.get(variant=self.variant).quantity, 20)

    def test_cannot_oversell(self):
        with self.assertRaises(InsufficientStockError):
            apply_movement(
                variant=self.variant, delta=-5,
                movement_type=StockMovement.Type.OUT, reason=StockMovement.Reason.SALE,
                user=self.user,
            )
        self.assertEqual(Stock.objects.get(variant=self.variant).quantity,0)

class StockApiTest(APITestCase):

    def setUp(self):
        self.admin = User.objects.create_user(username="a", password="x", role=User.Role.ADMIN)
        product = Product.objects.create(name="Widget")
        self.variant = ProductVariant.objects.create(product=product, price=5)
        self.stock = Stock.objects.get(variant=self.variant)
        self.client.force_authenticate(self.admin)

    def test_receive_endpoint_increases_quanitiy(self):
        response = self.client.post(f"/api/stock/{self.stock.id}/receive/", {"quantity":10})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.stock.refresh_from_db()
        self.assertEqual(self.stock.quantity, 10)

    def test_issue_more_than_available_return_400_not_500(self):
        response = self.client.post(f"/api/stock/{self.stock.id}/issue/", {"quantity": 999})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_low_stock_filter(self):
        self.stock.reorder_level = 100
        self.stock.save()
        response = self.client.get("/api/stock/?low_stock=true")
        skus = [row["sku"] for row in response.data["results"]]
        self.assertIn(self.variant.sku,skus)