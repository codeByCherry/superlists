from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from .models import Item
from .models import List

from django.http import HttpResponse


def home_page(request):
    return render(request, 'lists/home_page.html')


def view_list(request, list_id):
    list_ = get_object_or_404(List, pk=list_id)
    items = list_.item_set.all()
    context = dict(
        items=items,
        list_id=list_.id,
    )
    return render(request, 'lists/list.html', context)


def new_list(request):
    if request.method == "POST":
        list1 = List.objects.create()
        item_text = request.POST.get('item_text')
        Item.objects.create(list=list1, text=item_text)
        return redirect(f'/lists/{list1.id}/')

    else:
        raise Exception('Only accept POST request!!!')


def add_item(request, list_id):
    cur_list = get_object_or_404(List, pk=list_id)

    if request.method == "POST":
        item_text = request.POST.get('item_text')
        Item.objects.create(list=cur_list, text=item_text)
        return redirect(f'/lists/{cur_list.id}/')

    else:
        raise Exception('Only accept POST reqeust!!!')
