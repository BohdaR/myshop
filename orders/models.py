from django.db import models
from shop.models import Product


DELIVERY_CHOICES=[
        ('delivery1','Доставка до відділення Нової Пошти'),
        ('delivery2','Доставка кур\'єром'),
        ('delivery3','Адресна доставка кур\'єром "Нова Пошта"'),
        ]

PAY_CHOICES=[
    ('pay1','Оплата картою'),
    ('pay2','Оплата готівкою'),
]

class Order(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Ім\'я')
    last_name = models.CharField(max_length=50, verbose_name='Прізвище')
    email = models.EmailField(verbose_name='Електронна пошта')
    address = models.CharField(max_length=250, verbose_name='Адреса')
    phone_number = models.CharField(max_length=20, verbose_name='Телефон')
    city = models.CharField(max_length=100, verbose_name='Місто')
    delivery_method = models.CharField(choices=DELIVERY_CHOICES, max_length=50, default='delivery1', verbose_name='Спосіб доставки')
    pay_method = models.CharField(choices=PAY_CHOICES, max_length=50, default='pay1', verbose_name='Спосіб оплати')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'замовлення'
        verbose_name_plural = 'Замовлення'

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.PROTECT)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)


    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity

