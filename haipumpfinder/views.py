from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Hospital


class IndexView(generic.ListView):
    template_name = 'haipumpfinder/index.html'
    context_object_name = 'hospital_list'
    def get_queryset(self):
        """Return all published hospitals."""
        return Hospital.objects.order_by('id')

class DetailView(generic.DetailView):
    model = Hospital
    template_name = 'haipumpfinder/detail.html'

class ResultsView(generic.DetailView):
    template_name = 'haipumpfinder/what-the-hai.html'

class ResultsView(generic.DetailView):
    template_name = 'haipumpfinder/news.html'

#class Address_List(Hospitals)
#     @property
#    def get_address(self):
#        address_list = []  
#        for hospital in Hospital.objects.all()
#          address_list = address_list.append[hospital.city]  
#        endfor 
#        return address_list