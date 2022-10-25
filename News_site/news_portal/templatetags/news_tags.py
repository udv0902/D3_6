from django import template  # импортируем модуль template для работы с шаблонами
from news_portal.models import *  # импортируем модели которые есть в приложении news_portal

# создаем экземпляр класса Library, через который происходит регистрация собственных шаблонных тэгов
register = template.Library()


# функция для работы тэга
# чтобы функция get_categories была доступна по другому имени, для этого в параметрах указываем name='getcats'
@register.simple_tag(name='getcats')
def get_categories(filter=None):
	if not filter:  # если фильтр имеет значение None
		return Category.objects.all()  # обращение к базе данных и выборка из таблицы Category всех записей
	else:
		return Category.objects.filter(pk=filter)  # иначе выбираем записи по главному ключу которые соответствуют
# значению filter


@register.inclusion_tag('news_portal/list_categories.html')
# первый параметр функции sort=None сортировка категорий, второй cat_selected=0 определяет какая категория будет выбрана
def show_categories(sort=None, cat_selected=0):
	if not sort:  # если сортировка не определена
		cats = Category.objects.all()  # выводим все категории
	else:
		cats = Category.objects.order_by(sort)  # иначе делаем сортировку по указанному значению sort
	return {'cats': cats, 'cat_selected': cat_selected}  # второй параметр передаем шаблону list_categories.html
# чтобы проверить какая категория выбрана и отобразить её как обычный текст.


@register.filter(name='censor')
def censor(value):
	bad_words = ['выдающиеся', 'алгоритмы', 'сортировки', 'программисты', 'функции']
	if not isinstance(value, str):
		raise TypeError(f"unresolved type '{type(value)}' expected type 'str'")

	for word in value.split():
		if word.lower() in bad_words:
			value = value.replace(word, f"{word[0]}{'*' * (len(word) - 1)}")
	return value
