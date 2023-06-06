from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from item.models import Item, Category
import re

# Create your views here.
@login_required
def index(request):
    items = Item.objects.filter(createdBy=request.user)
    itemCategories = {}
    
    for item in items:

        if item.category.name not in itemCategories.keys():
            itemCategories[item.category.name] = 0
        itemCategories[item.category.name] += 1


    print(itemCategories.keys())

    return render(request, 'dashboard/index.html', {
        'items': items,
        'itemCategories': itemCategories,
    })
