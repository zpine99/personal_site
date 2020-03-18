from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Post, Comment
from .forms import CommentForm


def blog_index(request):
    object_list = Post.objects.all().order_by('-created_on')
    paginator = Paginator(object_list, 3)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    return render(request, 'blog/blog_index.html', {'page_number': page_number,
                                                    'page_obj': page_obj})


def blog_category(request, category):
    posts = Post.objects.filter(categories__name__contains=category).order_by('-created_on')
    context = {
        'category': category,
        'posts': posts,
    }
    return render(request, 'blog/blog_category.html', context)


def blog_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data['author'],
                body=form.cleaned_data['body'],
                post=post
            )
            comment.save()
        return HttpResponseRedirect(reverse('blog:blog_detail', args=(post.id,)))

    comments = Comment.objects.filter(post=post)
    context = {
        'post': post,
        'comments': comments,
        'form': form,
    }
    return render(request, 'blog/blog_detail.html', context)