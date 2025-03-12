from django.urls import path
from .views import *

urlpatterns = [
    path('user/', Userview.as_view()),
    path('user/<int:id>/', UserviewByid.as_view()),
    path('products/', ProductView.as_view()),
    path('products/<int:id>/',ProductViewbyId.as_view()),
    path('category/', CategoryViewbyId.as_view()),
    path('category/<int:id>/', CategoryDelete.as_view()),

]