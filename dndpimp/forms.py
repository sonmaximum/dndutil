from django.forms import ModelForm
from dndpimp.models import Item

class ItemForm(ModelForm):
	class Meta:
		model = Item
		fields = ('name', 'description',)