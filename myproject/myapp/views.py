from django.shortcuts import render, get_object_or_404
from .models import User, Order
from datetime import datetime, timedelta


def index(request):
    context = {'title': 'Main',
               'h1': 'Главная страница сайта',
               'h2': 'Сайт сделан на Django',
               }
    return render(request, 'myapp/index.html', context)


def about(request):
    context = {'title': 'About me',
               'fio': 'Иванов Иван Ивановчи',
               'phone': '+7(999) 999-99-99',
               'adress': 'г Москва, ул. Тверская 1'
               }
    return render(request, 'myapp/about.html', context)


def orders(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    orders = Order.objects.filter(customer_id=user_id)
    context = {"user": user, "orders": orders, "title": "Все заказы пользователя"}
    return render(request, 'myapp/orders.html', context)


def order_last_days(request, user_id):
    days = [7, 30, 365]
    result = {}
    user = User.objects.filter(pk=user_id).first()
    for day in days:
        last_day = datetime.now() - timedelta(days=day)
        orders = Order.objects.filter(customer_id=user, date_ordered__gte=last_day)
        products = set()
        for order in orders:
            for product in order.products.all():
                products.add(product)
        result[day] = products
    context = {"7days": result[7],
               "30days": result[30],
               "365days": result[365],
               "title": "Товары за 7, 30, 365 дней",
               "user": user,
               }
    return render(request, 'myapp/orders_last_days.html', context)
