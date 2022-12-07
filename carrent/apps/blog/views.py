from django.http import Http404
from django.shortcuts import render, redirect
from .models import Blog, Category, Tags, Author, Paragraph
from apps.comment.models import Comment
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def blog(request):
    posts = Blog.objects.all().order_by('-id')

    cat = request.GET.get('cat')
    tag = request.GET.get('tag')
    author = request.GET.get('author')
    date = request.GET.get('date')
    q = request.GET.get('q')
    page_number = request.GET.get('page')
    if cat:
        posts = posts.filter(category__title__exact=cat)

    if tag:
        posts = posts.filter(tags__title__exact=tag)

    if author:
        posts = posts.filter(author__username__exact=author)

    if q:
        posts = posts.filter(title__icontains=q)

    if date:
        posts = posts.filter(created_at__contains=date)

    p = Paginator(posts, 1)
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(3)
    except EmptyPage:
        page_obj = p.page(p.num_pages)

    context = {
        'posts': posts,
        'page_obj': page_obj,
    }
    return render(request, 'blog.html', context)


def blog_single(request, pk=None):
    if request.method == "POST":
        if request.user.is_authenticated:
            message = request.POST.get('message')
            comment_id = request.POST.get('comment_id')
            top_level_comment_id = request.POST.get('top_level_comment_id')

            if message:
                comment = Comment(
                    author_id=request.user.id,
                    post_id=pk,
                    message=message
                )
                if comment_id:
                    comment.parent_id = comment_id
                if top_level_comment_id:
                    comment.top_level_comment_id = top_level_comment_id
                comment.save()
                return redirect(f'/blog/{pk}#comment-list')
        return redirect('/login/')

    if pk is not None:
        post = Blog.objects.get(id=pk)
        cats = Category.objects.all()
        authors = Author.objects.all()
        paragraphs = Paragraph.objects.all()
        comments = Comment.objects.filter(is_reply=False, post_id=pk)
        context = {
            'post': post,
            'cats': cats,
            'authors': authors,
            'paragraphs': paragraphs,
            'comments': comments,
        }

        return render(request, 'single.html', context)
    raise Http404
