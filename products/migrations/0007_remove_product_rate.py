# Generated by Django 4.0.4 on 2022-07-10 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='rate',
        ),
    ]