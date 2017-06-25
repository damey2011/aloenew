"""truealoehealth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from truealoehealth import views

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^discounts/', views.DiscountView.as_view(), name='discount'),
    url(r'^upload/', views.upload, name='upload'),
    url(r'^become-business-owner/', views.BecomeBusinessOwnerView.as_view(), name='become-owner'),
    url(r'^products/', include('products.urls'), name='products'),
    url(r'^feedback/', include('feedback.urls'), name='feedback'),
    url(r'^top-products/', include('topproducts.urls'), name='top-products'),
    url(r'^blogs/', include('blogs.urls'), name='blogs'),
    url(r'^admin/', admin.site.urls)
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
