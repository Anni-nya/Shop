from django.shortcuts import render, get_object_or_404
#from django.http import HttpResponse
from .models import Category, Product
from cart.forms import CartAddProductForm

def product_list(request, category_slug = None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available = True)
    if category_slug:
        category = get_object_or_404(Category, slug = category_slug)
        products = products.filter(category = category)
    return render(request, 'start_django/list.html',
                  {'category':category,
                          'categories':categories,
                          'products': products
                   })
def product_detail(request, id, slug):
    product = get_object_or_404(Product, id = id, slug = slug, available = True)
    cart_product_form = CartAddProductForm()
    return render(request, 'start_django/detail.html',{
            'product': product,
            'cart_product_form': cart_product_form
            })


from flask import Flask, request
import git

app = Flask(__name__)

@app.route('/update_server', methods=['POST'])
def webhook():
    if request.method == 'POST':
        repo = git.Repo('https://github.com/Anni-nya/Shop')
        origin = repo.remotes.origin

        origin.pull()

        return 'Updated PythonAnywhere successfully', 200
    else:
        return 'Wrong event type', 400