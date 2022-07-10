from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator,MaxValueValidator



class Category(models.Model):
    name = models.CharField(max_length=100)
    slug= models.SlugField(unique=True)
    
    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('category', args=[self.slug])

class Product(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image1 = models.ImageField(upload_to='products/')
    image2 = models.ImageField(upload_to='products/')
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('product_detail', args=[self.slug])

class Rating(models.Model):
    product = models.ForeignKey(Product, related_name='rates', on_delete=models.CASCADE)
    rate = models.IntegerField(validators=[MinValueValidator(1),
     MaxValueValidator(5)], default=0)


    def __str__(self):
        return f'{self.product.title}:{self.rate}'
