from unicodedata import name
from django.urls import path

from . import views


urlpatterns = [
    path('',views.master_login, name='master_login'),
    path('master_home/',views.master_home,name='master_home'),
    path('master_logout/',views.master_logout,name='master_logout'),
    path('add_user/',views.add_user,name='add_user'),
    path('view_user/',views.view_user,name='view_user'),
    path('edit_user/<int:id>',views.edit_user,name='edit_user'),
    path('delete_user/<int:id>',views.delete_user,name='delete_user'),
 

]
 
