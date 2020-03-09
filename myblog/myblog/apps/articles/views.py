from django.urls import reverse
from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from .models import Article


def index(request):
    latest_articles_list = Article.objects.order_by('-pud_date')[:5]  # Выведет список последних 5 статей
    return render(request, 'articles/list.html',
                  {'latest_articles_list': latest_articles_list})  # передаем в шаблон


def detail(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except:
        raise Http404("Статья не найдена")

    latest_comments_list =a.comment_set.order_by('-id')[:10]#Возварщаем список комментов последние 10
    return render(request, 'articles/detail.html', {'article': a, 'latest_comments_list':latest_comments_list})#Возвращаем список статей



def leave_comment(request, article_id):  #Оставление комментариев
    try:
        a = Article.objects.get(id=article_id)
    except:
        raise Http404("Статья не найдена")

    a.comment_set.create(author_name=request.POST['name'],
                         comment_text=request.POST['text'])
    return HttpResponseRedirect(reverse('articles:detail', args=(a.id,)))  #возвращение на траницу при  обновлении после написания комментария