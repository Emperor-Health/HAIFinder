from django.shortcuts import get_object_or_404, render, HttpResponse, Http404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.template import Context, Template 
from django.urls import reverse
from django.views import generic  
from .forms import SignUpForm
from accounts.forms import PatientForm

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

    
def profile_view(request): 
    page_title = "Magnesium & Scorn - Profile - A New Way to Fight Your Cancer"
    form = PatientForm()
    return render(request, 'haipumpfinder/profile.html', {'form': form, 'page_title': page_title})
     