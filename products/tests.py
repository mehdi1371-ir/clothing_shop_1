from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from .models import Product, Category


class ProductTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.category = Category.objects.create(name='mens')
        cls.product = Product.objects.create(
            title = 'product1',
            slug = 'product_1',
            description = 'description of product1',
            image1 = SimpleUploadedFile(name='test_image.jpg', content=open('media/products/men-02_hjzZU1E.jpg', 'rb').read(), content_type='image/jpeg'),
            image2 = SimpleUploadedFile(name='test_image.jpg', content=open('media/products/men-02_vHkUNdj.jpg', 'rb').read(), content_type='image/jpeg'),
            price = 25.55,
            category = cls.category,
        )

    def test_product_model_str(self):
        product = self.product
        self.assertEqual(str(product), product.title)