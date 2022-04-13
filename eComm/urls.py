from django.urls import path
from . import views


urlpatterns = [
    # Login Or Welcome Page
    path('', views.frontPage, name='front'),

    # Login Or Welcome Page
    path('eComm/', views.index, name='index'),

    # Shop Page
    path('eComm/shop/', views.shop, name='shop'),

    # Books Page
    path('eComm/books/', views.books, name='books'),

    # Contact Page
    path('eComm/contact/', views.contact, name='contact'),

    path('eComm/action-and-adventure/', views.action, name='action'),

    path('eComm/action-and-adventure/buy_now', views.buy_now, name='buy_now'),

    path('eComm/historical_fiction/buy_now', views.buy_now, name='buy_now'),

    path('eComm/historical_fiction/', views.historical_fiction, name='historical_fiction'),

    path('eComm/detective_mystery/', views.detective_mystery, name='detective_mystery'),

    path('eComm/detective_mystery/buy_now', views.buy_now, name='buy_now'),

    path('eComm/shortBooks/', views.shortBooks, name='shortBooks'),

    path('eComm/shortBooks/buy_now', views.buy_now, name='buy_now'),

    path('eComm/action-and-adventure/fantasy_simulator/congratulations', views.congratulations, name='congratulations'),


]