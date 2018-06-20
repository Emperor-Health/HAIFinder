from django.shortcuts import get_object_or_404, render, HttpResponse, Http404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.template import Context, Template 
from django.urls import reverse
from django.views import generic
# Create your views here.

def index(request): 
    page_title = "Magnesium & Scorn Personalized Trialfinder"
    trial1 = {
            'nct_id': 'NCT11111111', 
            'trial_name': 'Pembrolizumab in MMR-Proficient Metastatic Colorectal Cancer Pharmacologically Primed to Trigger Dynamic Hypermutation Status',
            'phase': '2',
            'date_added': '01/31/2018',
            'locations': 'United States',
            'immuno': 'Yes',
            'prior_immuno': 'No',
            'crc': 'Yes',
            'status': 'Recruiting',
            'drugs': 'Keytruda, Imfinzi, Alimta, Paraplatin',
            }
    trial2 = {
            'nct_id': 'NCT03531632', 
            'trial_name': 'MGD007 Combined With MGA012 in Relapsed/Refractory Metastatic Colorectal Cancer (NCT03531632)',
            'phase': 'Phase 1/Phase 2',
            'date_added': '2018-05-09',
            'locations': 'North Carolina',
            'immuno': 'Yes',
            'prior_immuno': 'No',
            'crc': 'Yes',
            'status': 'Not Yet Recruiting',
            'drugs': 'MGD007 + MGA012',
            }
    trials_list = trial1, trial2, trial1, trial2, trial1
    trials_dict = {
        'trials_list': trials_list,
        'page_title': page_title,
    }
    return render(request,'index.html', trials_dict)
