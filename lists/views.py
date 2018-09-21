from django.shortcuts import render
from django.shortcuts import redirect
from .models import Item
from django.http import HttpResponse


# Create your views here.
def home_page(request):
    if request.method == "POST":
        item_text = request.POST.get('item_text')
        Item.objects.create(text=item_text)
        return redirect('/')

    items = Item.objects.all()
    context = dict(
        items=items,
    )
    return render(request, 'lists/home_page.html', context)
