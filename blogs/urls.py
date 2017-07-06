from django.conf.urls import url
from blogs import views

urlpatterns = [
    url(r'^$', views.AllBlogs.as_view(), name='all-blogs'),
    url(r'^compose/', views.ComposeBlogPost.as_view(), name='compose-post'),
    url(r'^update/(?P<post_id>\d+)/$', views.UpdateBlogPost.as_view(), name='update-post'),
    url(r'^save-comment/', views.SaveComment.as_view(), name='save-comment'),
    url(r'^(?P<slug>[\w-]+)/$', views.BlogPostView.as_view(), name='blog-post'),
]
