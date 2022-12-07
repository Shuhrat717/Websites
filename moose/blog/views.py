from django.shortcuts import render, redirect
from .models import *
from contact.models import Subscribe
from .forms import CommentForm


def home(request):
    posts = Article.objects.filter(is_published=True)
    author = About.objects.all()
    email = request.POST.get('email')
    if request.method == 'POST':
        Subscribe.objects.create(email=email)
    context = {
        'author': author,
        'posts': posts,
        'email': email,
    }
    return render(request, 'index.html', context)


def about(request):
    person = Article.objects.all()
    email = request.POST.get('email')
    if request.method == 'POST':
        Subscribe.objects.create(email=email)
    context = {
        'person': person,
        'email': email,
    }
    return render(request, 'about.html', context)


def blog(request):
    posts = Article.objects.all().order_by('-id')
    email = request.POST.get('email')
    if request.method == 'POST':
        Subscribe.objects.create(email=email)
    context = {
        'posts': posts,
        'email': email,
    }
    return render(request, 'blog.html', context)


def blog_single(request, slug):
    post = Article.objects.get(slug=slug)
    author = About.objects.all()
    email = request.POST.get('email')
    if request.method == 'POST':
        Subscribe.objects.create(email=email)
    comments = Comment.objects.filter(article__slug__exact=slug).order_by('-id')
    form = CommentForm(request.POST or None, request.FILES)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.article = post
        comment.user = request.user
        comment.save()
        return redirect(f'blog_single/{post.slug}#comment')
    context = {
        'author': author,
        'post': post,
        'email': email,
        'comments': comments,
        'form': form,
    }
    return render(request, 'blog-single.html', context)







