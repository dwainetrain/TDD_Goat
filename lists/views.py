from django.shortcuts import redirect, render

from django.core.exceptions import ValidationError

from lists.forms import ItemForm, EMPTY_ITEM_ERROR
from lists.models import Item, List

# Create your views here.
def home_page(request):
    return render(request, 'home.html', {'form': ItemForm()})

# def new_list(request):
#     list_ = List.objects.create()
#     item = Item(text = request.POST['text'], list = list_)
#     try:
#         item.full_clean()
#         item.save()
#     except ValidationError:
#         list_.delete()
#         error = "You can't have an empty list item"
#         return render(request, 'home.html', {'error': error})
#     return redirect(list_)

def new_list(request):
    form = ItemForm(data=request.POST)
    if form.is_valid():
        list_ = List.objects.create()
        Item.objects.create(text=request.POST['text'], list=list_)
        return redirect(list_)
    else:
        return render(request, 'home.html', {"form": form})

def view_list(request, list_id):
    list_ = List.objects.get (id = list_id)
    form = ItemForm()

### editing pg 250 ###
    if request.method == 'POST':
        try:
            item = Item(text=request.POST['text'], list=list_)
            item.full_clean()
            item.save()
            return redirect(list_)
        except ValidationError:
            error = EMPTY_ITEM_ERROR

    form = ItemForm()
    return render (request, 'list.html', {
        'list': list_, "form": form, "error": error
        })