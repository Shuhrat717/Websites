from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .models import Article, Tags, Category
from apps.comments.forms import CommentForm


def blog_single(request):
    return render(request, 'blog-single.html')


def index(request):
    categories = Category.objects.all()
    object_list = Article.objects.all().order_by('-id')
    posts = Article.objects.all()
    for category in categories:
        category.n = len(Article.objects.filter(category=category))
    p = Paginator(posts, 2)
    page = request.GET.get('page')
    posts_ = p.get_page(page)
    context = {
        'categories': categories,
        'object_list': object_list,
        'p': p,
        'posts': posts_,
        'posts_category': posts[:3:-1],
    }

    return render(request, 'index.html', context)


def views_up(request, pk):
    article = Article.objects.get(id=pk)
    article.save()
    return redirect('articles:single', article.pk)


def article_single(request, pk):
    article = Article.objects.get(id=pk)
    categories = Category.objects.all()
    recent_articles = Article.objects.all().order_by('-id')[:3]
    tags = Tags.objects.all()
    form = CommentForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.article_id = pk
        obj.save()
        return redirect(f'/blog-detail/{pk}#article-comments')
    context = {
        'object': article,
        'categories': categories,
        'recent_articles': recent_articles,
        'tags': tags,
        'form': form,
    }
    return render(request, 'blog-single.html', context)


def article_view(request):
    articles = Article.objects.all().order_by('-id')

    tag = request.GET.get('tag')
    category = request.GET.get('category')
    q = request.GET.get('q')
    if tag:
        articles = articles.filter(tags__title__exact=tag)
    if category:
        articles = articles.filter(category__title__exact=category)

    if q:
        articles = articles.filter(title__exact=q)

    context = {
        'object_list': articles
    }

    return render(request, 'blog.html', context)
