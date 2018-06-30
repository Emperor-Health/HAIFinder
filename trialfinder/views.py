from django.shortcuts import get_object_or_404, render, HttpResponse, Http404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.template import Context, Template 
from django.urls import reverse
from django.views import generic
from .services import get_trials  
# Create your views here.

def index(request): 
         
        #print("Trial Name: " + trial_name)
        page_title = "Trial Finder" 
        trials_list = get_trials()  

        trials_dict = { 
                'trials_list': trials_list,
                'page_title': page_title,
        }
        return render(request,'index.html', trials_dict)
