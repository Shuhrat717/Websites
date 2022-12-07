from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator


def home(request):
    cats = Category.objects.all()
    zone_cat = ZoneCat.objects.all()
    posts = Article.objects.filter(is_published=True)
    for cat in cats:
        cat.n = len(Article.objects.filter(cat=cat))
    p = Paginator(posts, 2)
    page = request.GET.get('page')
    posts_ = p.get_page(page)
    context = {
        'cats': cats,
        'zone_cat': zone_cat,
        'p': p,
        'posts': posts_,
        'posts_cat': posts[:3:-1],
    }

    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')


def category(request, pk):
    posts_pop = Article.objects.all().order_by('-views')[:3]
    cats = Category.objects.all()
    zone_cat = ZoneCat.objects.all()
    for cat in cats:
        cat.n = len(Article.objects.filter(cat=cat))

    cat = Category.objects.get(id=pk)
    posts = Article.objects.filter(cat=cat).filter(is_published=True)

    context = {
        'cats': cats,
        'zone_cat': zone_cat,
        'posts_car': posts[:3:-1],
        'posts_pop': posts_pop,
        'posts': posts,
        'cat': cat,
    }
    return render(request, 'category.html', context)


def blog_single(request, slug):
    posts_pop = Article.objects.all().order_by('-id')[:3]
    cats = Category.objects.all()
    zone_cat = ZoneCat.objects.all()
    posts = Article.objects.filter(is_published=True)
    for cat in cats:
        cat.n = len(Article.objects.filter(cat=cat))

    obj = Article.objects.get(slug=slug)
    obj.views += 1
    obj.save()

    context = {

        'cats': cats,
        'zone_cat': zone_cat,
        'posts_car': posts[:3:-1],
        'posts_pop': posts_pop,

        'obj': obj,
    }
    return render(request, 'blog-single.html', context)

