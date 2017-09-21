from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from .models import Item, Comment
from .forms import ItemForm, CommentForm


def index(request):
    items = Item.objects.order_by('-created_date')
    context = {'items': items}
    return render(request, 'tracker/index.html', context)

def create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            item = Item(title=title, description=description)
            item.save()

            return HttpResponseRedirect(reverse('index'))
    else:
        form = ItemForm()

    return render(request, 'tracker/create.html', {'form': form})

def detail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    return render(request, 'tracker/detail.html', {'item':item})

def comment(request, item_id):
    item = Item.objects.get(pk=item_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            comment = Comment(item=item, text=text)
            comment.save()

            return HttpResponseRedirect(reverse('detail', kwargs={'item_id':item_id}))

    else:
        form = CommentForm()

    return render(request, 'tracker/comment.html', {'form': form, 'item': item})
