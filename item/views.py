from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from item.models import Item, Category
from .forms import NewItemForm, EditItemForm


def browse(request):
    query = request.GET.get('query', '') # 默认值为空 ‘’
    items = Item.objects.filter(isSold=False)
    categories = Category.objects.all()
    category_id = request.GET.get('category', 0) # 默认值为零 0

    if category_id:
        items = items.filter(category_id=category_id)

    if query:
        # 标准写法：property + __icontains
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request, 'item/browse.html', {
        'items': items,
        'query': query,
        'categories': categories,
        'category_id': int(category_id),
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
