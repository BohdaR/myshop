# Generated by Django 4.0.2 on 2022-03-15 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_alter_product_available'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-updated', '-created', '-id'], 'verbose_name': 'товар', 'verbose_name_plural': 'Товари'},
        ),
    ]
