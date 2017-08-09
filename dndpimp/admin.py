from django.contrib import admin

# Register your models here.
from dndpimp.models import Item

class ItemAdmin(admin.ModelAdmin):
	model = Item
	list_display = ('name', 'description',)
	prepopulated_fields = {'slug': ('name',)}
		
		
admin.site.register(Item, ItemAdmin)
