from django.shortcuts import render


# Create your views here.


# The front page url function
def frontPage(request):
    return render(request, 'frontPage.html')


# The home url function
def index(request):
    return render(request, 'index.html')


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

