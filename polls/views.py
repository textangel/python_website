#from django.http import HttpResponse

#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")

from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)
