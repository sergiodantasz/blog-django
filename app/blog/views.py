from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import Http404
from django.shortcuts import render

from blog.models import Page, Post

PER_PAGE = 9


def index(request):
    posts = Post.objects.get_published()
    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': page_obj,
            'page_title': 'Home - '
        }
    )


def created_by(request, author_pk):
    user = User.objects.filter(pk=author_pk).first()
    if user is None:
        raise Http404()
    posts = Post.objects.get_published().filter(created_by__pk=author_pk)
    if user.first_name:
        user_full_name = f'{user.first_name} {user.last_name}'
    else:
        user_full_name = user.username
    page_title = f'{user_full_name}\'s Posts - '
    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': page_obj,
            'page_title': page_title
        }
    )


def category(request, slug):
    posts = Post.objects.get_published().filter(category__slug=slug)
    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    if len(posts) == 0:
        raise Http404()
    page_title = f'{page_obj[0].category.name} - Category - '
    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': page_obj,
            'page_title': page_title
        }
    )


def page(request, slug):
    page_ = Page.objects.filter(is_published=True).filter(slug=slug).first()
    if page_ is None:
        raise Http404()
    page_title = f'{page_.title} - Page - '
    return render(
        request,
        'blog/pages/page.html',
        {
            'page': page_,
            'page_title': page_title
        }
    )


def post(request, slug):
    post_ = Post.objects.get_published().filter(slug=slug).first()
    if post_ is None:
        raise Http404()
    page_title = f'{post_.title} - Post - '
    return render(
        request,
        'blog/pages/post.html',
        {
            'post': post_,
            'page_title': page_title
        }
    )


def tag(request, slug):
    posts = Post.objects.get_published().filter(tag__slug=slug)
    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    if len(posts) == 0:
        raise Http404()
    page_title = f'{page_obj[0].tag.first().name} - Tag - '
    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': page_obj,
            'page_title': page_title
        }
    )


def search(request):
    search_value = request.GET.get('search', '').strip()
    posts = Post.objects.get_published().filter(
        Q(title__icontains=search_value) |
        Q(excerpt__icontains=search_value) |
        Q(content__icontains=search_value)
    )
    page_title = f'{search_value} - Search - '
    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': posts,
            'search_value': search_value,
            'page_title': page_title
        }
    )
