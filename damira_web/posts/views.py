from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Article
from django.http import JsonResponse
from django.db.models import Q

def index(request):
    articles = Article.objects.all().order_by('-created_at')[:2]
    random_articles = Article.objects.all().order_by('?')[:8]
    return render(request, 'index.html', {'articles' : articles, 'random_articles': random_articles})

def article(request, urlName):
    read_too = Article.objects.all().order_by('-created_at')[:4]
    article = get_object_or_404(Article, urlName=urlName)
    return render(request, 'article.html', {'article': article, 'read_too': read_too})

def articles(request):
    query = request.GET.get('szukaj')
    if query:
        articles_list = Article.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query) | Q(description__icontains=query)
        )
    else:
        articles_list = Article.objects.all().order_by("-created_at")
    
    paginator = Paginator(articles_list, 7)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    current_page = page_obj.number
    total_pages = paginator.num_pages

    if total_pages <= 10:
        start_page = 1
        end_page = total_pages
    else:
        if current_page <= 5:
            start_page = 1
            end_page = 10
        elif current_page + 4 >= total_pages:
            start_page = total_pages - 9
            end_page = total_pages
        else:
            start_page = current_page - 5
            end_page = current_page + 4

    pages_range = range(start_page, end_page + 1)

    # Определяем, нужно ли показывать ссылки на предыдущий и следующий набор страниц
    show_prev_set = start_page > 1
    show_next_set = end_page < total_pages

    return render(request, 'articles.html', {
        'page_obj': page_obj,
        'pages_range': pages_range,
        'show_prev_set': show_prev_set,
        'show_next_set': show_next_set,
        'prev_set_start': max(1, start_page - 10),
        'next_set_start': min(total_pages, end_page + 1),
    })



def cookies(request):
    return render(request, 'cookies.html')

def contact(request):
    return render(request, 'contact.html')
