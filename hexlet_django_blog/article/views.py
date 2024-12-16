from django.views import View
from django.shortcuts import render

class ArticlePageView(View):
        
    items = [
        {'article_id': 1, 'tag': 'fiction', 'author': 'J.K. Rowling', 'work': 'Harry Potter', 'date': '1982-04-03'},
        {'article_id': 2, 'tag': 'fiction', 'author': 'Eliezer Judkowskiy', 'work': 'Harry Potter but Rationalised', 'date': '2011-10-17'},
        {'article_id': 42, 'tag': 'python'}
    ]

    template_articles = 'article/index.html'
    template_one_article = 'article/one_article.html'
    
    def get_item(self, article_id, tag):
        for item in self.items:
            if item['article_id'] == article_id and item['tag'] == tag:
                return item
        raise ValueError('Article not found')

    def get(self, request, article_id=None, tag=None, *args, **kwargs):
        if article_id and tag:
            return render(request, template_name=self.template_one_article, context={'item': self.get_item(article_id, tag)})
        return render(request, template_name=self.template_articles, context={'items': self.items})