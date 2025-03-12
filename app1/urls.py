
from django.contrib import admin
from django.urls import path,include
from . import views
from .views import *
# from .views import Home
# from .views import add
# from .views import f1
# from .views import cat


urlpatterns = [
    # path('hello/', Home), 
    # path('html/',add),
    # path('js/',f1),
    path('home/',Homepage),
    # path('product/',Product_lists),
    # path('productadd/',ProductAdd),
    path('product/', views.Product_lists, name='product_list'),  # Ensure this exists
    path('productadd/', views.ProductAdd, name='product_add'),
]
