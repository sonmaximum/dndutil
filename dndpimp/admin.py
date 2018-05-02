from django.contrib import admin

# Register your models here.
from dndpimp.models import *


class ItemAdmin(admin.ModelAdmin):
    model = Item
    list_display = ('name', 'description',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Item, ItemAdmin)


class CharacterAdmin(admin.ModelAdmin):
    model = Character
    list_display = ('name', 'description', 'party', 'user')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Character, CharacterAdmin)


class PartyAdmin(admin.ModelAdmin):
    model = Party
    list_display = ('name', 'description',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Party, PartyAdmin)
