from django.shortcuts import get_object_or_404, render, HttpResponse, Http404, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.template import Context, Template 
from django.urls import reverse
from django.views import generic  
from .forms import SignUpForm
from accounts.forms import PatientForm, UserForm
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.conf import settings

# Create your views here.
def signup(request):
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
        form = SignUpForm()
        #print('Form wasnt valid')
        #print(form)
        page_title = "Magnesium & Scorn - Sign up - A New Way to Find Help Fighting Your Cancer"
    return render(request, 'haipumpfinder/signup.html', {'form': form, 'page_title': page_title})

def logout_view(request):
    print("Got here");
    if request.user.is_authenticated:
        logout(request)
    page_title = "Magnesium & Scorn - Sign up - A New Way to Fight Your Cancer"
    form = SignUpForm()
    return render(request, 'haipumpfinder/signup.html', {'form': form, 'page_title': page_title})

def success(request):
    return render(request, 'haipumpfinder/success.html')


def login_view(request): 
    print("Got here"); 
    if request.user.is_authenticated:
        logout(request)
    page_title = "Magnesium & Scorn - Sign up - A New Way to Fight Your Cancer"
    form = SignUpForm()
    return render(request, 'haipumpfinder/login.html', {'form': form, 'page_title': page_title})

@login_required
@transaction.atomic   
def profile_view(request): 
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        patient_form = PatientForm(request.POST, instance=request.user.patient)
        if user_form.is_valid() and patient_form.is_valid():
            user_form.save()
            patient_form.save()
            #messages.success(request, _('Your profile was successfully updated!'))
            return redirect('haipumpfinder:profile')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        u_p = request.user.patient
        u = request.user
   
        page_title = "Magnesium & Scorn - Profile - A New Way to Fight Your Cancer"
        patient_form = PatientForm(request.POST or None, instance=u_p)
        user_form = UserForm(request.POST or None, instance=u)

    return render(request, 'haipumpfinder/profile.html', {
        'user_form': user_form,
        'patient_form': patient_form, 
        'page_title': page_title})

 
@login_required    
def treatment_add(request): 
    page_title = "Magnesium & Scorn - Add a treatment "
    form = PatientForm()
    return render(request, 'haipumpfinder/treatmentadd.html', {'form': form, 'page_title': page_title})
     