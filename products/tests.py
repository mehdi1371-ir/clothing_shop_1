from email.mime import image
import tempfile
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from .models import Product, Category


class ProductTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.category = Category.objects.create(name='mens')
        cls.image1 = tempfile.NamedTemporaryFile(suffix=".jpg").name
        cls.image2 = tempfile.NamedTemporaryFile(suffix=".jpg").name
        cls.product = Product.objects.create(
            title = 'product1',
            slug = 'product_1',
            description = 'description of product1',
            price = 25.55,
            image1 = cls.image1,
            image2 = cls.image2,
            category = cls.category,
        )

    def test_product_model_str(self):
        product = self.product
        self.assertEqual(str(product), product.title)

    def test_product_objects(self):
        self.assertEqual(self.product.title, 'product1')
        self.assertEqual(self.product.description, 'description of product1')
        self.assertEqual(self.product.slug, 'product_1')
        self.assertEqual(self.product.price, 25.55)
        self.assertEqual(self.product.image1, self.image1)
        self.assertEqual(self.product.image2, self.image2)
        self.assertEqual(self.product.category, self.category)