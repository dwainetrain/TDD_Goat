from django.shortcuts import redirect, render

from django.core.exceptions import ValidationError

from lists.forms import ExistingListItemForm, ItemForm, EMPTY_ITEM_ERROR
from lists.models import Item, List

from django.contrib.auth import get_user_model
User = get_user_model()

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
        list_ = List()
        list_.owner = request.user
        list_.save()
        form.save(for_list=list_)
        return redirect(list_)
    else:
        return render(request, 'home.html', {"form": form})

def view_list(request, list_id):
    list_ = List.objects.get (id = list_id)
    form = ExistingListItemForm(for_list=list_)
    if request.method == 'POST':
        form = ExistingListItemForm(for_list=list_, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(list_)
    return render(request, 'list.html', {'list': list_, "form": form})

def my_lists(request, email):
    owner = User.objects.get(email=email)
    return render(request, 'my_lists.html', {'owner': owner})