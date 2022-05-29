from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Image(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/')


    
