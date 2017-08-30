from django.shortcuts import render, redirect
from dndpimp.forms import *
from dndpimp.models import *
from django.template.defaultfilters import slugify

# Create your views here.
def index(request):
	items = Item.objects.all()
	return render(request, 'index.html', {
		'items': items,
	})

def create_item(request):
	form_class = ItemForm
	if request.method == 'POST':
		form = form_class(request.POST)
		if form.is_valid():
			item = form.save(commit=False)
			item.user = request.user
			item.slug = slugify(item.name)
			item.save()
			return redirect('item_detail', slug=item.slug)
	else:
		form = form_class()

	return render(request, 'characters/create_character.html', {
		'form': form,
		})

def item_detail(request, slug ):
	item = Item.objects.get(slug=slug)
	return render (request, 'items/item_detail.html', {
		'item': item
		})

def edit_item(request, slug):
	item = Item.objects.get(slug=slug)
	form_class = ItemForm
	if request.method == 'POST':
		form = form_class(data=request.POST, instance=item)
		if form.is_valid():
			form.save()
			return redirect('item_detail', slug=item.slug)

	else:
		form = form_class(instance=item)

	return render(request, 'items/edit_item.html', {
		'item': item,
		'form': form,
	})

def create_character(request):
	form_class = CharacterForm
	if request.method == 'POST':
		form = form_class(request.POST)
		if form.is_valid():
			character = form.save(commit=False)
			character.user = request.user
			character.slug = slugify(character.name)
			character.save()
			return redirect('character_detail', slug=character.slug)
	else:
		form = form_class()

	return render(request, 'characters/create_character.html', {
		'form': form,
		})

def character_detail(request, slug ):
	character = Character.objects.get(slug=slug)
	return render (request, 'characters/character_detail.html', {
		'character': character
		})

def edit_character(request, slug):
	character = Character.objects.get(slug=slug)
	form_class = CharacterForm
	if request.method == 'POST':
		form = form_class(data=request.POST, instance=character)
		if form.is_valid():
			form.save()
			return redirect('character_detail', slug=character.slug)

	else:
		form = form_class(instance=character)

	return render(request, 'characters/edit_character.html', {
		'character': character,
		'form': form,
		})
