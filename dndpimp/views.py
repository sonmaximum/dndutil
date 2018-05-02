from django.shortcuts import render, redirect
from dndpimp.forms import *
from dndpimp.models import *
from django.template.defaultfilters import slugify
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.template import Context
from django.http import Http404


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


def item_detail(request, slug):
    item = Item.objects.get(slug=slug)
    return render(request, 'items/item_detail.html', {
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


def character_detail(request, slug):
    character = Character.objects.get(slug=slug)
    return render(request, 'characters/character_detail.html', {
        'character': character
        })


@login_required
def edit_character(request, slug):
    character = Character.objects.get(slug=slug)
    if character.user != request.user:
        raise Http404

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


def browse_by_name(request, initial=None):
    if initial:
        items = Item.objects.filter(
            name__istartswith=initial).order_by('name')
    else:
        items = Item.objects.all().order_by('name')
    return render(request, 'search/search.html', {
        'items': items,
        'initial': initial,
    })


def contact(request):
    form_class = ContactForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = form.cleaned_data['contact_name']
            contact_email = form.cleaned_data['contact_email']
            form_content = form.cleaned_data['content']

            # email the profile with the contact info
            template = get_template('contact_template.txt')

            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            }
            content = template.render(context)

            email = EmailMessage(
                'New contact form submission',
                content,
                'Your website DND PIMP',
                ['maxjuchheim@gmail.com'],
                headers={'Reply-To': contact_email}
            )
            email.send()
            return redirect('contact')

    return render(request, 'contact.html', {
        'form': form_class,
    })
