from django.contrib import admin

# Register your models here.
from dndpimp.models import Treasure

class TreasureAdmin(admin.ModelAdmin):
	model = Treasure
	list_display = ('name', 'description',)
	prepopulated_fields = {'slug': ('name',)}
		
		
admin.site.register(Treasure, TreasureAdmin)
