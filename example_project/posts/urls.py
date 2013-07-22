from guardian.compat import url, patterns


urlpatterns = patterns('posts.views',
    url(r'^$', view='post_list', name='posts_post_list'),
    url(r'^comments/?$', view='comment_list', name='posts_comment_list'),
    url(r'^(?P<slug>[-\w]+)/$', view='post_detail', name='posts_post_detail'),
    url(r'^comments/(?P<comment_id>\d+)$', view='comment_detail', name='posts_comment_detail'),
)

