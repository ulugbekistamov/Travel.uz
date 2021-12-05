from django.shortcuts import render
from django.views import generic
from .models import *



class LadingPageView(generic.TemplateView):
    template_name = 'index.html'

class viloyatPageView(generic.TemplateView):
    template_name = 'viloyat.html'

class TeatrPageView(generic.TemplateView):
    template_name = 'teatr.html'

class RestoranPageView(generic.TemplateView):
    template_name = 'restoran.html'

class MaskanPageView(generic.TemplateView):
    template_name = 'maskan.html'

class HotelPageView(generic.TemplateView):
    template_name = 'hotel.html'

class HotelmainPageView(generic.TemplateView):
    template_name = 'hotel-main.html'


def create_viloyat(request):
    viloyat = Viloyat.objects.all()
    context = {
        "viloyat": viloyat
    }
    return render(request, "mai.html", context)
















