import locale

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader

from blogsite.forms import PostForm
from blogsite.models import Post


def post_list(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    template = loader.get_template('blog/post_list.html')
    locale.setlocale(locale.LC_ALL, 'russian_russia')
    for post in posts:
        post.pub_date = post.pub_date.strftime("%d %B %Y %H:%M")
    context = {
        'mainPost': posts[0],
        'posts': posts,
    }
    return HttpResponse(template.render(context, request))


def post_view(request):
    template = loader.get_template('blog/post_add.html')
    context = {
        'bread': 'Добавить статью',
    }
    return HttpResponse(template.render(context, request))


def post_add(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse({'result': 'ok'})
    return JsonResponse({'result': 'false'})
