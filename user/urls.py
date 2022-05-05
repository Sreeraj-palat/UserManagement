from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path('',views.user_login, name='user_login'),
    path('user_home/',views.user_home,name='user_home'),
    path('user_logout/',views.user_logout,name='user_logout'),
    path('reg_user/',views.reg_user,name='reg_user'),
    path('add_product/',views.add_product,name='add_prod'),  
    path('edit_product/<str:pk>',views.edit_product,name='edit_prod'),
    path('delete_product/<str:pk>',views.delete_product,name='delete_prod'),
]