# из django импортируем функцию path чтобы формировать наши маршруты
# импортируем функцию re_path для использования регулярных выражений
from django.urls import path, re_path

from .views import *  # из файла views.py импортируем все функции представления

urlpatterns = [
	path('', news_portalHome.as_view(), name='home'),  # http://127.0.0.1:8000/news_portal/
	# path('cats/<int:catid>/', categories),  # http://127.0.0.1:8000/news_portal/cats/
	# сначала должен идти префикс archive, потом год состоящий из 4ёх цифр использующий цыфры от 0 до 9, потом сама функция обработчик archive
	# re_path(r'^archive/(?P<year>[0-9]{4})/', archive),
	path('about/', about, name='about'),
	path('add_page/', AddPage.as_view(), name='add_page'),
	path('contact/', contact, name='contact'),
	path('login/', login, name='login'),
	path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
	path('category/<slug:cat_slug>/', news_portalCategory.as_view(), name='category'),
]
