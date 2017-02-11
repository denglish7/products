from django.shortcuts import render, redirect
from .models import Product
from ..log_reg.models import User
from django.contrib import messages

def index(request):
    if 'user_id' not in request.session:
        return redirect("log_reg:index")

    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'my_wishlist': Product.objects.filter(user_products__id=request.session['user_id'])|Product.objects.filter(all_users__id=request.session['user_id']),
        'others_wishlist': Product.objects.all().exclude(user_products__id=request.session['user_id']).exclude(all_users__id=request.session['user_id'])
    }
    return render(request, "first_app/index.html", context)

def logoff(request):
    request.session.clear()
    return redirect("log_reg:index")

def add_page(request):
    if 'user_id' not in request.session:
        return redirect("log_reg:index")

    return render(request, "first_app/add.html")

def add_product(request):
    res = Product.objects.validate(request.POST)

    if res['added']:
        Product.objects.create(name=request.POST['name'], user_products=User.objects.get(id=request.session['user_id']))
    else:
        for error in res['errors']:
            messages.error(request, error)
        return redirect('first_app:add_page')

    return redirect("first_app:index")

def show(request, id):
    if 'user_id' not in request.session:
        return redirect("log_reg:index")
        
    context = {
        'product': Product.objects.get(id=id),
        'other_users': User.objects.filter(all_products__id=id)|User.objects.filter(products_of_user__id=id)
    }
    return render(request, "first_app/show.html", context)

def add_to_list(request, id):
    user = User.objects.get(id=request.session['user_id'])
    product = Product.objects.get(id=id)
    product.all_users.add(user)
    return redirect("first_app:index")

def remove_from_list(request, id):
    user = User.objects.get(id=request.session['user_id'])
    product = Product.objects.get(id=id)
    product.all_users.remove(user)
    return redirect("first_app:index")

def delete(request, id):
    Product.objects.get(id=id).delete()
    return redirect("first_app:index")
