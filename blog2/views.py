from django.shortcuts import render
from django.utils import timezone
from .models import Post


# Create your views here.


def post_list(request):
    # get a QuerySet of posts that aren't in the future,
    # ordered by when they were published
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # pass the posts to the template
    return render(request, 'blog2/post_list.html', {'posts': posts})
