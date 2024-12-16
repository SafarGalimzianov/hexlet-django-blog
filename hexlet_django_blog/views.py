from django.views.generic.base import TemplateView
from django.shortcuts import redirect, render
from django.urls import reverse

class HomePageView(TemplateView):

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['who'] = 'Safar'
        return context

def about(request):
    return render(request, 'about.html')

def to_redirect(request):
    return redirect(reverse('article', kwargs={'tag': 'python', 'article_id': 42}))