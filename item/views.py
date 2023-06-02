from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from item.models import Item
from .forms import NewItemForm, EditItemForm


def browse(request):
    items = Item.objects.filter(isSold=False)

    return render(request, 'item/browse.html', {
        'items': items
    })




# Create your views here.
def detail(request, primaryKey):
    item = get_object_or_404(Item, pk=primaryKey)
    related_items = Item.objects.filter(category=item.category, isSold=False).exclude(pk=primaryKey)[0:3]

    return render(request, 'item/detail.html', {
        'item': item,
        'related_items': related_items
    })


@login_required
def new(request):

    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False) # createdBy 没有被指明，database 会报错
            item.createdBy = request.user
            item.save()

            return redirect('item:detail', primaryKey=item.id)
            # return redirect('')

    else:
        form = NewItemForm()



    return render(request, 'item/form.html', {
        'form': form,
        'title': 'New item',
    })



@login_required
def delete(request, primaryKey):
    item = get_object_or_404(Item, pk=primaryKey, createdBy=request.user)
    item.delete()

    return redirect('dashboard:index')



@login_required
def edit(request, primaryKey):
    item = get_object_or_404(Item, pk=primaryKey, createdBy=request.user)


    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()

            return redirect('item:detail', primaryKey=item.id)


    else:
        form = EditItemForm(instance=item)



    return render(request, 'item/form.html', {
        'form': form,
        'title': 'Edit item',
    })
