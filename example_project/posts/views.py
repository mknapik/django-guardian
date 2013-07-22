from django.contrib.auth.models import Group
from django.shortcuts import render_to_response, get_object_or_404
from django.views.generic import ListView
from django.template import RequestContext
from guardian.decorators import permission_required_or_403
from guardian.compat import get_user_model

from .models import Post, Comment

User = get_user_model()


class PostList(ListView):
    model = Post
    context_object_name = 'posts'


class CommentList(ListView):
    model = Comment
    context_object_name = 'comments'


post_list = PostList.as_view()
comment_list = CommentList.as_view()


@permission_required_or_403('posts.view_post', (Post, 'slug', 'slug'))
def post_detail(request, slug, **kwargs):
    data = {
        'post': get_object_or_404(Post, slug=slug),
        'users': User.objects.all(),
        'groups': Group.objects.all(),
    }
    return render_to_response('posts/post_detail.html', data,
                              RequestContext(request))


@permission_required_or_403('posts.view_comment', (Comment, 'id', 'comment_id'))
def comment_detail(request, comment_id, **kwargs):
    data = {
        'comment': Comment.objects.get(pk=comment_id),
        'users': User.objects.all(),
        'groups': Group.objects.all(),
    }
    return render_to_response('posts/comment_detail.html', data,
                              RequestContext(request))

