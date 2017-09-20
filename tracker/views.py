from django.shortcuts import render

from .models import Item, Comment

def index(request):
    items = Item.objects.order_by('-created_date')
    context = {'items': items}
    return render(request, 'tracker/index.html', context)

