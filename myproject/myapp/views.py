from django.shortcuts import render
from django.http import HttpResponse


def index(response):
    html = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Main</title>
        </head>
        <body>
            <h1 style="text-align: center;">Главная страница сайта</h1>
            <h2 style="text-align: center;">Сайт сделан на Django</h2>
        </body>
        </html>
    """
    return HttpResponse(html)


def about(response):
    html = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>About</title>
        </head>
        <body>
            <h1 style="text-align: center;">Обо мне</h1>
            <div style="margin-left: 40px;">
                <p>ФИО:</p>
                <h3>Иванов Иван Иванович</h3>
                <p>Телефон:</p>
                <h3>+7(999) 999-99-99</h3>
                <p>Адрес:</p>
                <h3>г Москва, ул. Тверская 1</h3>
            </div>
        </body>
        </html>
    """
    return HttpResponse(html)
