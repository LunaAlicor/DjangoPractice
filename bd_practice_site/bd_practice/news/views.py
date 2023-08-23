from django.shortcuts import render
from .models import Articles
from django.views.generic import DetailView

# Create your views here.


def news(request):
    news = Articles.objects.all().order_by('-date')
    return render(request, 'news/news.html', {'news': news})


class NewsDetail(DetailView):
    model = Articles
    template_name = 'news/news_details.html'
    context_object_name = 'article'
