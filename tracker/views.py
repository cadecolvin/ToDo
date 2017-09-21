from django.shortcuts import render

from .models import Item, Comment
from .forms import ItemForm


def index(request):
    items = Item.objects.order_by('-created_date')
    context = {'items': items}
    return render(request, 'tracker/index.html', context)

def create_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            item = Item(title=title, description=description)
            item.save()
    else:
        form = ItemForm()

    return render(request, 'tracker/newitem.html', {'form': form})
