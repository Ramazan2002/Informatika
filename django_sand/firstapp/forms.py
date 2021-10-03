from django import forms

SIZES = (
	('xxs', 'XXS'),
	('xs', 'XS'),
	('s', 'S'),
	('m', 'M'),
	('l', 'L'),
	('xl', 'XL'),
	('xxl', 'XXL')
)

class SimpleTextForm(forms.Form):
	name = forms.CharField(label='Имя',max_length=35)
	age = forms.IntegerField(label='Возраст')
	height = forms.FloatField(label='Рост')
	weight = forms.FloatField(label='Вес')
	size = forms.ChoiceField(choices = SIZES, widget=forms.RadioSelect)