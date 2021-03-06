# Generated by Django 4.0.2 on 2022-03-16 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_alter_characteristic_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.AlterField(
            model_name='characteristic',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='product_image', to='shop.product'),
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='products/%Y/%m/%d', verbose_name='Зображення товару')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='characteristic_items', to='shop.product')),
            ],
            options={
                'verbose_name': 'зображення товару',
                'verbose_name_plural': 'зображення товару',
            },
        ),
    ]
