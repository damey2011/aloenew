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
    url(r'^test/', views.Test.as_view(), name='test'),
    url(r'^aloe-vera-drink/', views.AloeVeraDrink.as_view(), name='aloe'),
    url(r'^aloe-vera-nutrition/', views.AloeVeraNutrition.as_view(), name='nutrition'),
    url(r'^aloe-vera-cosmetics/', views.AloeVeraCosmetics.as_view(), name='cosmetics'),
    url(r'^aloe-vera-skincare/', views.AloeVeraSkinCare.as_view(), name='skincare'),
    url(r'^aloe-vera-bee-products/', views.AloeVeraBeeProducts.as_view(), name='bee_products'),
    url(r'^aloe-vera-combo-packs/', views.AloeVeraComboPacks.as_view(), name='combo'),
    url(r'^aloe-vera-personal-care/', views.AloeVeraPersonal.as_view(), name='personal'),
    url(r'^aloe-vera-weight-management/', views.AloeVeraWeight.as_view(), name='weight'),
    url(r'^gluten-free-products/', views.GlutenFree.as_view(), name='gluten'),
    url(r'^forever-i-t-weight-loss/', views.FIT.as_view(), name='fit'),
    url(r'^clean-9/', views.Clean9.as_view(), name='c9'),
    url(r'^clean-9-instructions/', views.C9Instructions.as_view(), name='c9-inst'),
    url(r'^admin/', admin.site.urls)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
