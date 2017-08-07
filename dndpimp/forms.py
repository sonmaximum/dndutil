from django.forms import ModelForm
from dndpimp.models import Treasure

class TreasureForm(ModelForm):
	class Meta:
		model = Treasure
		fields = ('name', 'description',)