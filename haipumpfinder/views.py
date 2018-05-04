from django.shortcuts import get_object_or_404, render, HttpResponse
from django.http import HttpResponseRedirect
from django.template import Context, Template
from django.urls import reverse
from django.views import generic
#import pdb; pdb.set_trace()
from .services import Trial, TrialLocation
from .models import Hospital
 





def trial(request,trial_id):
    t = Trial()
    trial_name = t.get_name(trial_id) 
    #print("Trial Name: " + trial_name)
    sites_list = t.get_locations(trial_id) 
    #print(len(sites_list))
    sites_dict = {
        'sites_list': sites_list,
        'trial_name': trial_name,
        'trial_id': trial_id,
         

    }
    return render(request,'haipumpfinder/trial.html', sites_dict)

# console.log('Got here bitch!')
#sites_list = Trial.locations('NCT02928224')
#print("Sites Count: " + sites_list[0].city)
#return HttpResponse("Got test to Trial!")
#return render(request,'trial.html',sites_list) 



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