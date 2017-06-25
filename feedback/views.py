from django.shortcuts import render

# Create your views here.
from django.views import View
from feedback.models import FeedBack


class FeedBackView(View):
    def get(self, request):
        return render(request, 'contacts.html', {'contact': 'current'})

    def post(self, request):
        name = request.POST['contactName']
        email = request.POST['email']
        comments = request.POST['comments']

        feedback = FeedBack(name=name, email=email, message=comments)
        feedback.save()

        return render(request, 'feedback_sent.html')
