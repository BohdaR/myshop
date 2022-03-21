from django.urls import path
from . import views


urlpatterns = [
    path('', views.cart_detail, name='wish_list_detail'),
    path('add/<int:product_id>/', views.cart_add, name='wish_list_add'),
    path('remove/<int:product_id>/', views.cart_remove, name='wish_list_remove'),
]