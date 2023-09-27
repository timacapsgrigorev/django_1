from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def index(request):
    logger.info("Посещение главной страницы")

    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Моя главная страница</title>
    </head>
    <body>
        <h1>Добро пожаловать на мой сайт</h1>
        <p>Здесь вы найдете информацию обо мне и моем проекте.</p>
        <a href="/about/">О себе</a>
    </body>
    </html>
    """
    return HttpResponse(html)


def about(request):
    logger.info("Посещение страницы 'О себе'")

    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Обо мне</title>
    </head>
    <body>
        <h1>Обо мне</h1>
        <p>Здесь вы найдете информацию обо мне.</p>
        <a href="/">Главная</a>
    </body>
    </html>
    """
    return HttpResponse(html)
