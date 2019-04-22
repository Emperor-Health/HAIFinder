from django.urls import path, include
from django.views.generic import TemplateView
from array import array
from django.conf.urls import url
from django.contrib import admin 
from django.contrib.auth import views as auth_views
from accounts import views as accounts_views
from trialfinder import views as trialfinder_views
from haipumpfinder import views as HPViews
app_name = 'haipumpfinder'

urlpatterns = [
    path(r'what-the-hai', TemplateView.as_view(template_name="haipumpfinder/what-the-hai.html")),
    path(r'hai-in-the-news', TemplateView.as_view(template_name="haipumpfinder/news.html")),
    path('', HPViews.IndexView.as_view(), name='index'),
    path('<int:pk>/', HPViews.DetailView.as_view(), name='detail'),
    path(r'trial/<str:trial_id>', HPViews.trial, name='trial'),
    path(r'signup/', accounts_views.signup, name='signup'),  
    path(r'success/', accounts_views.success, name='success'),
    path(r'profile/', accounts_views.profile_view, name='profile'), 
    
    path(r'detail-treatment/', accounts_views.detail_treatment, name='detail_treatment'),   
    path(r'add-treatment/', accounts_views.add_treatment, name='add_treatment'), 
    path(r'password_change/', auth_views.password_change, name='password_change'),   
    path(r'logout/', auth_views.logout, name='logout'),    
    path(r'login/', auth_views.login, name='login'), 
    path(r'trial/<str:trial_id>', HPViews.trial, name='treatment'),
    #path('accounts/', include('django.contrib.auth.urls')),
 ]