from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home_page(request):
    if request.method == "POST":
        item_text = request.POST.get('item_text')
        return render(request, 'lists/home_page.html', context={'new_item_text': item_text})
    return render(request, 'lists/home_page.html')
