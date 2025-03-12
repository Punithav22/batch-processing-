from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product
from .form import ProductForm  # Ensure this is correctly defined in form.py


def Homepage(request):
    context = {
        'fruits': ['apple', 'banana', 'cherry'],
    }
    return render(request, 'index11.html', context)  # Simplified, no need for loader


def Product_lists(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'prolist.html', context)


def ProductAdd(request):
    form = ProductForm(request.POST or None)  # Fixed incorrect `Productform`

    if form.is_valid():
        form.save()
        return redirect('product_list')  # Use the correct named URL

    return render(request, 'form.html', {'form': form})





# def Home(request):

#     # return HttpResponse("Hello")
#     return render(request ,'login.html')

# def add (self):
#     return render (self,'sample.html')

# def f1 (request):
#     return render(request,'sample.html')


# def cat(request):
#     return render(request,'sample.html')