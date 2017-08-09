from django.forms import ModelForm
from dndpimp.models import *

class ItemForm(ModelForm):
	class Meta:
		model = Item
		fields = ('name', 'description',)

class CharacterForm(ModelForm):
	class Meta:
		model = Character
		fields = ('name', 'description',)