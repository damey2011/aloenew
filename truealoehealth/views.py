from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from blogs.models import BlogPost
from products.models import StandAloneImageUpload
from django.shortcuts import render_to_response
from django.template import RequestContext


class HomeView(View):
    def get(self, request):
        posts = BlogPost.objects.all().order_by('?')[:3]
        return render(request, 'home.html', {'home': 'current', 'posts': posts})


class DiscountView(View):
    def get(self, request):
        posts = BlogPost.objects.all().order_by('?')[:3]
        return render(request, 'discounts.html', {'discounts': 'current', 'posts': posts})


class BecomeBusinessOwnerView(View):
    def get(self, request):
        posts = BlogPost.objects.all().order_by('?')[:3]
        return render(request, 'become-distributor.html', {'become': 'current', 'posts': posts})


class Test(View):
    def get(self, request):
        posts = BlogPost.objects.all().order_by('?')[:3]
        return render(request, 'new-blog-list.html', {'posts': posts})


class AloeVeraDrink(View):
    def get(self, request):
        return render(request, 'products-dropdown/aloe-vera-drinks.html', {'products': 'current'})


class AloeVeraNutrition(View):
    def get(self, request):
        return render(request, 'products-dropdown/nutrition.html', {'products': 'current'})


class AloeVeraCosmetics(View):
    def get(self, request):
        return render(request, 'products-dropdown/cosmetics.html', {'products': 'current'})


class AloeVeraSkinCare(View):
    def get(self, request):
        return render(request, 'products-dropdown/skin-care.html', {'products': 'current'})


class AloeVeraBeeProducts(View):
    def get(self, request):
        return render(request, 'products-dropdown/bee.html', {'products': 'current'})


class AloeVeraComboPacks(View):
    def get(self, request):
        return render(request, 'products-dropdown/combo.html', {'products': 'current'})


class AloeVeraPersonal(View):
    def get(self, request):
        return render(request, 'products-dropdown/personal.html', {'products': 'current'})


class AloeVeraWeight(View):
    def get(self, request):
        return render(request, 'products-dropdown/weight-management.html', {'products': 'current'})


class GlutenFree(View):
    def get(self, request):
        return render(request, 'products-dropdown/gluten-free.html', {'products': 'current'})


class FIT(View):
    def get(self, request):
        posts = BlogPost.objects.all().order_by('?')[:3]
        return render(request, 'fit.html', {'fit': 'current', 'posts': posts})


class Clean9(View):
    def get(self, request):
        posts = BlogPost.objects.all().order_by('?')[:3]
        return render(request, 'c9.html', {'clean': 'current', 'posts': posts})


class C9Instructions(View):
    def get(self, request):
        posts = BlogPost.objects.all().order_by('?')[:3]
        return render(request, 'c9-instructions.html', {'clean': 'current', 'posts': posts})


@csrf_exempt
def upload(request):
    # folder = 'uploads'

    # uploaded_filename = request.FILES['image'].name
    uploaded_file = request.FILES['upload']

    to_be_uploaded = StandAloneImageUpload()
    to_be_uploaded.image = uploaded_file

    to_be_uploaded.save()
    image_url = to_be_uploaded.image.url

    # return JsonResponse(image_url, safe=False)

    return JsonResponse({'uploaded': 1, 'fileName': to_be_uploaded.image.name, 'url': image_url})


def handler404(request):
    response = render_to_response('404.html', {}, context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request):
    response = render_to_response('500.html', {}, context_instance=RequestContext(request))
    response.status_code = 500
    return response
