from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from .models import BlogPost, Like, Comment, Reply

def index(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog_list.html', {'posts': posts})

@login_required
def like_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    like, created = Like.objects.get_or_create(user=request.user, post=post)

    if not created:  
        like.delete()  # اگر قبلاً لایک کرده باشد، آن را حذف می‌کنیم.
        liked = False
    else:
        liked = True

    return JsonResponse({'liked': liked, 'like_count': post.likes.count()})


@login_required
def add_comment(request, post_id):
    if request.method == "POST":
        post = get_object_or_404(BlogPost, id=post_id)
        content = request.POST.get('content')
        if content:
            comment = Comment.objects.create(user=request.user, post=post, content=content)
            return JsonResponse({'user': comment.user.username, 'content': comment.content, 'comment_id': comment.id})
    return JsonResponse({'error': 'Invalid request'}, status=400)


@login_required
def add_reply(request, comment_id):
    if request.method == "POST":
        comment = get_object_or_404(Comment, id=comment_id)
        content = request.POST.get('content')
        if content:
            reply = Reply.objects.create(user=request.user, comment=comment, content=content)
            return JsonResponse({'user': reply.user.username, 'content': reply.content, 'reply_id': reply.id})
    return JsonResponse({'error': 'Invalid request'}, status=400)
