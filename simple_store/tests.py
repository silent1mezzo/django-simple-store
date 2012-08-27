from django.utils import unittest
from django.core.urlresolvers import reverse
from django.test.client import Client
from simple_store.models import Product, Category

class ProductTestCase(unittest.TestCase):

    def setUp(self):
        self.client = Client()

    """
        Test Product Creation Assumptions
    """
    def test_creation_assumptions(self):
        product = Product.objects.create(name="Test", description="Test Product")

        self.assertEqual(product.slug, 'test')
        self.assertEqual(product.sku, 'test')

    def test_index(self):
        resp = self.client.get(reverse('store'))
        self.assertEqual(resp.status_code, 200)

    def test_category(self):
        category = Category.objects.create(name="Test", description="Test Category")

        resp = self.client.get(reverse('category', args=[category.slug]))
        self.assertEqual(resp.status_code, 200)

        resp = self.client.get(reverse('category', args=['non_existent_slug']))
        self.assertEqual(resp.status_code, 404)
