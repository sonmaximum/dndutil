from django.shortcuts import render, redirect
from dndpimp.forms import TreasureForm
from dndpimp.models import Treasure

# Create your views here.
def index(request):
	treasures = Treasure.objects.all()
	return render(request, 'index.html', {
		'treasures': treasures,
	})

def treasure_detail(request, slug ):
	treasure = Treasure.objects.get(slug=slug)
	return render (request, 'treasures/treasure_detail.html', {
		'treasure': treasure
		})

def edit_treasure(request, slug):
	treasure = Treasure.objects.get(slug=slug)
	form_class = TreasureForm
	if request.method == 'POST':
		form = form_class(data=request.POST, instance=treasure)
		if form.is_valid():
			form.save()
			return redirect('treasure_detail', slug=treasure.slug)

	else:
		form = form_class(instance=treasure)

	return render(request, 'treasures/edit_treasure.html', {
		'treasure': treasure,
		'form': form,
	})