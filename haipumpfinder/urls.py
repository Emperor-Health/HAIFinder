from django.urls import path
from django.views.generic import TemplateView
from array import array
from django.conf.urls import url
from django.contrib import admin 

from accounts import views as accounts_views
from haipumpfinder import views as HPViews
app_name = 'haipumpfinder'

urlpatterns = [
    path(r'what-the-hai', TemplateView.as_view(template_name="haipumpfinder/what-the-hai.html")),
    path(r'hai-in-the-news', TemplateView.as_view(template_name="haipumpfinder/news.html")),
    path('', HPViews.IndexView.as_view(), name='index'),
    path('<int:pk>/', HPViews.DetailView.as_view(), name='detail'),
    path(r'trial/<str:trial_id>', HPViews.trial, name='trial'),
    path(r'signup/', HPViews.signup, name='signup'), 
   
    #path('<int:question_id>/vote/', views.vote, name='vote'),
]