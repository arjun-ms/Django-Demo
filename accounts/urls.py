from django.urls import path
from . import views

urlpatterns = [
    # http://127.0.0.1:8000/accounts/register/
    path('register',views.register,name='register'),
    path('login',views.login,name='login')
    
]