from django.views import View
from django.shortcuts import render

class ArticlePageView(View):
        
    items = [
        {'author': 'J.K. Rowling', 'work': 'Harry Potter', 'date': '1982-04-03'},
        {'author': 'Eliezer Judkowskiy', 'work': 'Harry Potter but Rationalised', 'date': '2011-10-17'},
    ]

    template = 'article/index.html'
    
    def get(self, request, *args, **kwargs):
        return render(request, template_name=self.template, context={'items': self.items})