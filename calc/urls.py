from django.urls import path
from . import views

urlpatterns = [
    # http://127.0.0.1:8000/products/
    path('',views.index,name='index'),
    # http://127.0.0.1:8000/add
    path('add',views.add,name='add')
]