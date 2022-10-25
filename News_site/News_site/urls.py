"""News_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static  # импорт для функции static
from django.contrib import admin
from django.urls import path, include  # импортируем функцию include

from News_site import settings  # импорт для модуля settings
from news_portal.views import *

urlpatterns = [
	path('admin/', admin.site.urls),
	# path('', index),  # подключается функция index из файла views.py
	# path('cats/', categories),  # подключается функция cats из файла views.py
	path('', include('news_portal.urls'))  # передаем функции include маршруты нашего приложения news_portal
]
# Если в модуле settings.py DEBUG = True, то к маршрутам urlpatterns добавляем еще один маршрут для статических данных графических файлов: Указываем сначала адрес MEDIA_URL из файла settings, а затем корневую папку где непосредственно будут находиться файлы.
if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = pageNotFound  # переменной handler404 присваиваится функция pageNotFound из файла views.py. Обработчик
# handler будет работать только тогда, когда значение DEBUG = False в файле settings.py
