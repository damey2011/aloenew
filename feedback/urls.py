from django.conf.urls import url
from feedback import views

urlpatterns = [
    url(r'^$', views.FeedBackView.as_view(), name='fb')
]
