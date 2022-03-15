from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='Назва категорії')
    slug = models.SlugField(max_length=200, db_index=True, unique=True, verbose_name='URL')

    class Meta:
        ordering = ('name',)
        verbose_name = 'категорію'
        verbose_name_plural = 'Категорії'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_list_by_category',
                        args=[self.slug])


class Brend(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='Назва категорії')
    slug = models.SlugField(max_length=200, db_index=True, unique=True, verbose_name='URL')

    class Meta:
        ordering = ('name',)
        verbose_name = 'виробника'
        verbose_name_plural = 'виробники'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.PROTECT, verbose_name='Категорія товару')
    brend = models.ForeignKey(Brend, related_name='products', on_delete=models.PROTECT, verbose_name='бренд товару')
    name = models.CharField(max_length=200, db_index=True, verbose_name='Назва товару')
    slug = models.SlugField(max_length=200, db_index=True, unique=True, verbose_name='URL')
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, verbose_name='Зображення товару')
    description = models.TextField(blank=True, verbose_name='Опис товару')
    old_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name='Ціна до знижки')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Ціна товару')
    stock = models.PositiveIntegerField(verbose_name='Залишок товару')
    available = models.BooleanField(default=True, verbose_name='Доступність товару на складі')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        verbose_name = 'товар'
        verbose_name_plural = 'Товари'
        ordering = ['-updated', '-created', '-id']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail',
                        args=[self.slug])


class Characteristic(models.Model):
    product = models.ForeignKey('Product', related_name='characteristic_items', on_delete=models.PROTECT)
    name = models.CharField(max_length=200, db_index=True, verbose_name='назва характеристики')
    value = models.CharField(max_length=200, db_index=True, verbose_name='Значення характиристики')

    class Meta:
        verbose_name = 'характеристику'
        verbose_name_plural = 'характеристики'

    def __str__(self):
        return self.name