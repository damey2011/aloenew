from django.conf.urls import url
from topproducts import views

urlpatterns = [
    url(r'^$', views.TopProductsView.as_view(), name='prods')
]
