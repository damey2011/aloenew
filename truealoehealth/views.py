from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from products.models import StandAloneImageUpload
from django.shortcuts import render_to_response
from django.template import RequestContext


class HomeView(View):
    def get(self, request):
        return render(request, 'home.html', {'home': 'current'})


class DiscountView(View):
    def get(self, request):
        return render(request, 'discounts.html', {'discounts': 'current'})


class BecomeBusinessOwnerView(View):
    def get(self, request):
        return render(request, 'become-distributor.html', {'become': 'current'})


@csrf_exempt
def upload(request):
    # folder = 'uploads'
    print(request)
    print(request.FILES)

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

