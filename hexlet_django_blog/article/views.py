from django.shortcuts import render

items = [
    {'author': 'J.K. Rowling', 'work': 'Harry Potter', 'date': '1982-04-03'},
    {'author': 'Eliezer Judkowskiy', 'work': 'Harry Potter but Rationalised', 'date': '2011-10-17'},
]

# Create your views here.
def index(request):
    return render(request, "article/index.html", context={'items': items})