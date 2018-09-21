from django.shortcuts import render
from django.shortcuts import redirect
from .models import Item
from django.http import HttpResponse


UNIQUE_LIST = "/lists/unique-list/"


def home_page(request):
    if request.method == "POST":
        item_text = request.POST.get('item_text')
        Item.objects.create(text=item_text)
        return redirect(UNIQUE_LIST)

    items = Item.objects.all()
    context = dict(
        items=items,
    )
    return render(request, 'lists/home_page.html', context)


def view_list(request):
    items = Item.objects.all()
    context = dict(
        items=items,
    )
    return render(request, 'lists/view_list.html', context)

