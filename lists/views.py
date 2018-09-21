from django.shortcuts import render
from django.shortcuts import redirect
from .models import Item
from django.http import HttpResponse


UNIQUE_LIST = "/lists/unique-list/"


def home_page(request):
    return render(request, 'lists/home_page.html')


def view_list(request):
    if request.method == "POST":
        item_text = request.POST.get('item_text')
        Item.objects.create(text=item_text)
        return redirect(UNIQUE_LIST)

    items = Item.objects.all()
    context = dict(
        items=items,
    )
    return render(request, 'lists/list.html', context)


def new_list(request):
    if request.method == "POST":
        item_text = request.POST.get('item_text')
        Item.objects.create(text=item_text)
        return redirect(UNIQUE_LIST)

    else:
        raise Exception('Only accept POST request!!!')
