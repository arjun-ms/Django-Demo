from django.urls import path
from . import views

urlpatterns = [
    # http://127.0.0.1:8000/products/
    path('',views.index,name='index'),
    # http://127.0.0.1:8000/products/about
    path('about',views.about,name='about'),
    # http://127.0.0.1:8000/products/contact
    path('contact',views.contact,name='contact'),
    
    path('logout',views.logout,name='logout')
]