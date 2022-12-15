from django.shortcuts import render
from django.views import View


class ContactView(View):
    def get(self, request):
        return render(request, 'pages/contact.html')


class FaqView(View):
    def get(self, request):
        return render(request, 'pages/faq.html')