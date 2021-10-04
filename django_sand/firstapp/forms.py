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
	size = forms.ChoiceField(choices = SIZES, widget=forms.RadioSelect)