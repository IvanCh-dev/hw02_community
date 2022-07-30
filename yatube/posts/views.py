from django.shortcuts import render, get_object_or_404
from .models import Post, Group


def index(request):
    displayed_posts = 10
    title = 'Последние обновления на сайте'
    posts = Post.objects.select_related('group')[:displayed_posts]
    context = {
        'title': title,
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    displayed_posts = 10
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:displayed_posts]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
