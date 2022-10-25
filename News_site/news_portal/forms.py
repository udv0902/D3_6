from django import forms
from django.core.exceptions import ValidationError

from .models import *


# Класс создания формы добавления новости не связанной с моделью
class AddPostForm(forms.ModelForm):
	# title = forms.CharField(max_length=255, label='Заголовок')
	# slug = forms.SlugField(max_length=255, label='URL')
	# content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), label='Контент')
	# is_published = forms.BooleanField(label='Опубликовано', required=False, initial=True)
	# cat = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория', empty_label='Категория не выбрана')

	# Класс создания формы добавления новости связанной с моделью
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)  # вызов конструктора базового класса ModelForm
		self.fields['cat'].empty_label = 'Категория не выбрана'  # меняем свойство поля cat на empty_label

	# Чтобы не дублировать код полей при добавлении формы используем класс Meta в котором атрибут model делает связь с моделью news_portal, а второй атрибут fields = '__all__' говорит какие поля нужно отобразить в форме. Т.е. все поля кроме тех которые отображаются автоматически
	# На практике рекомендуется явно указывать список полей в создаваемой форме
	class Meta:
		model = news_portal
		# fields = '__all__'
		fields = ['title', 'slug', 'content', 'photo', 'is_published', 'cat']
		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-input'}),  # оформление полей ввода
			'content': forms.Textarea(attrs={'cols': 60, 'rows': 10})
		}

	# пользовательский валидатор для поля title
	def clean_title(self):
		title = self.cleaned_data['title']
		if len(title) > 200:
			raise ValidationError('Длина превышает 200 символов')
		return title
