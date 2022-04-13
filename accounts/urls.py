from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
    path('', views.accounts_Page, name='accounts_Page'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    
]