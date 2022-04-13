import string
from unicodedata import name
from django.db import models

# Create your models here.


class Destination:
    id: id
    name: str
    img: str
    desc: str
    price: float


class Shop_Page:
    title: str


class Contact_Page:
    name: str


