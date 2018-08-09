from django.shortcuts import get_object_or_404, render, HttpResponse, Http404, redirect, HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.template import Context, Template 
from django.urls import reverse
from django.views import generic        
from accounts.forms import PatientForm, UserForm, SignUpForm,   TreatmentForm 
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.conf import settings 
from django.views.generic import FormView, RedirectView
from haipumpfinder.models import Patient, Treatment

# Create your views here.
def signup(request):
    if request.user.is_authenticated:
        logout(request)
    page_title = "Magnesium & Hope - Sign up - A New Way to Find Help Fighting Your Cancer"
    if request.method == 'POST':
        form = SignUpForm(request.POST) 
        if form.is_valid(): 
            form.save()
            username = form.cleaned_data.get('username')
            #username = form.cleaned_data.get('email')
            
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect ('../success')
        else:
            messages.success(request, ('This user already exists'))
        return render(request, 'haipumpfinder/signup.html', {'form': form, 'page_title': page_title})
    else:
        form = SignUpForm()
        #print('Form wasnt valid')
        #print(form)

       
    return render(request, 'haipumpfinder/signup.html', {'form': form, 'page_title': page_title})

def login_view(request):
    print("Log IN Got hereXXX");
    if request.user.is_authenticated:
        logout(request)
    page_title = "Magnesium & Hope - Sign up - A New Way to Fight Your Cancer"
    form = SignUpForm()
    return render(request, 'haipumpfinder/login.html', {'form': form, 'page_title': page_title})


@login_required
def logout_view(request):
    print("LOG OUT Got here");
    if request.user.is_authenticated:
        logout(request)
    page_title = "Magnesium & Hope - Sign up - A New Way to Fight Your Cancer"
    form = SignUpForm()
    return HttpResponseRedirect('haipumpfinder/login.html')

def success(request):
    return render(request, 'haipumpfinder/success.html')

       
@login_required(login_url="../login/")
@transaction.atomic   
def profile_view(request): 
    page_title = "Magnesium & Hope - Update your Profile"
    #todo- LIST IS JUST ALL  
    treatment_list = Treatment.objects.filter(patient_id=request.user.patient.id)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        patient_form = PatientForm(request.POST, instance=request.user.patient)
        if user_form.is_valid() and patient_form.is_valid():
            user_form.save()
            patient_form.save()
            messages.success(request, ('Your profile was successfully updated!'))
            return redirect('haipumpfinder:profile')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        u_p = request.user.patient
        u = request.user
        patient_form = PatientForm(request.POST or None, instance=u_p)
        user_form = UserForm(request.POST or None, instance=u)

    return render(request, 'haipumpfinder/profile.html', {
        'user_form': user_form,
        'patient_form': patient_form, 
        'treatment_list': treatment_list,
        'page_title': page_title})

 

@login_required
@transaction.atomic     
def add_treatment(request):
    page_title = "Magnesium & Hope - Add a treatment "
    treatment_list = Treatment.objects.filter(patient_id=request.user.patient.id).order_by("start_date")
  
    print(request.POST)
    if request.method == 'POST': 
        treatment_form = TreatmentForm(request.POST)
        if treatment_form.is_valid():
            new_treatment = treatment_form.save(commit=False)
            print(new_treatment.description)
            new_treatment.patient_id = request.user.patient.id
            new_treatment.save()
            messages.success(request, ('Your treatment was successfully added!'))
            return redirect('haipumpfinder:add_treatment')
        else:

            messages.error(request, ('Please correct the error below.'))
    else: 
         
          #todo- LIST IS JUST ALL
     treatment_form = TreatmentForm()
    return render(request, 'haipumpfinder/treatmentadd.html', {'treatment_form':  treatment_form, 
    'treatment_list': treatment_list,
    'page_title': page_title})
     

@login_required
@transaction.atomic     
def detail_treatment(request):
    page_title = "Treatment Detail"
    return render(request, 'haipumpfinder/detailtreatment.html',
    {'page_title': page_title})