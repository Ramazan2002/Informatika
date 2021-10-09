from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

SIZES = (
	('xxs', 'XXS'),
	('xs', 'XS'),
	('s', 'S'),
	('m', 'M'),
	('l', 'L'),
	('xl', 'XL'),
	('xxl', 'XXL')
)

GENDERS = (
	('m', 'male'),
	('f', 'female'),
	('n', 'хз кто')
)

class SimpleTextForm(forms.Form):
	name = forms.CharField(max_length=35)
	age = forms.IntegerField()
	height = forms.FloatField()
	weight = forms.FloatField()
	gender = forms.ChoiceField(choices=GENDERS)
	size = forms.ChoiceField(choices = SIZES, widget=forms.RadioSelect, required=False)

	def clean_name(self):
		data = self.cleaned_data['name']
		if not data.isalpha():
			raise ValidationError(_('Имя должно содержать только буквы'), code='invalid')
		return data

	def clean_age(self):
		data = self.cleaned_data['age']
		if not 14 <= data <= 80:
			raise ValidationError(_('Возраст от 14 до 80 лет'), code='invalid')
		return data

	def clean_height(self):
		data = self.cleaned_data['height']
		if not 100 <= data <= 200:
			raise ValidationError(_('Рост от 100 до 200 см.'), code='invalid')
		return data

	def clean_weight(self):
		data = self.cleaned_data['weight']
		if not 30 <= data <= 200:
			raise ValidationError(_('Вес от 30 до 200'), code='invalid')
		return data
