from django.shortcuts import render
from .models import Articles
from django.views.generic import DetailView
from django.core.paginator import Paginator

# Create your views here.


def news(request):
    news_list = Articles.objects.all().order_by('-date')
    paginator = Paginator(news_list, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'news/news.html', {'page_obj': page_obj})


# def nonews(request):
#     return render(request, 'news/Nonews.html')


class NewsDetail(DetailView):
    model = Articles
    template_name = 'news/news_details.html'
    context_object_name = 'article'
