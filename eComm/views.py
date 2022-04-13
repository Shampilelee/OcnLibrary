from django.shortcuts import render
from eComm.models import Destination, Shop_Page

# Create your views here.


# The front page url function
def frontPage(request):
    return render(request, 'frontPage.html')


# The home url function
def index(request):

    dest1 = Destination()
    dest1.name = 'BOOKS'
    dest1.price = 700

    return render(request, 'index.html', {'dest1': dest1})


# The Shop Page
def shop(request):

    shop = Shop_Page()
    shop.title = 'Shop - Ocean Library'

    return render(request, 'shop.html', {'shop': shop})


# The Books Page
def books(request):
    return render(request, 'books.html')


# The Contact Page
def contact(request):
    return render(request, 'contact.html')


# Action And Adventure
def action(request):
    return render(request, 'action-and-adventure.html')


# Buy Now
def buy_now(request):
    return render(request, 'buy_now.html')


# historical-fiction
def historical_fiction(request):
    return render(request, 'historical-fiction.html')


# Detective and Mystery
def detective_mystery(request):
    return render(request, 'detective_mystery.html')


# Short Books
def shortBooks(request):
    return render(request, 'shortBooks.html')


# Congratulations Page
def congratulations(request):

    userEmail = request.POST['email']

    return render(request, 'congratulations.html', {'userEmail': userEmail})

