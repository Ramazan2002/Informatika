from django import forms


class SimpleTextForm(forms.Form):
	name = forms.CharField(label='Имя',max_length=35)
	age = forms.IntegerField(label='Возраст')
	height = forms.FloatField(label='Рост')
	weight = forms.FloatField(label='Вес')