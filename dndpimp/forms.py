from django import forms
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

class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea
    )

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label = 'Your name:'
        self.fields['contact_email'].label = 'Your email:'
        self.fields['content'].label = 'Your message:'
