from django.urls import path
from .views import index, about, orders, order_last_days, add_user, add_product

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('orders/<int:user_id>/', orders, name='orders'),
    path('order_last_days/<int:user_id>/', order_last_days, name='order_last_days'),
    path('user/add/', add_user, name='add_user'),
    path('product/add/', add_product, name='add_product'),
]