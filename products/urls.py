from django.conf.urls import url
from products import views

urlpatterns = [
    url(r'^$', views.ProductsView.as_view(), name='prods'),
    url(r'^categories/', views.ProductCategoriesList.as_view(), name='prod_cat'),
    url(r'^category/(?P<pk>\d+)/$', views.ProductCategoryView.as_view(), name='answer'),
]
