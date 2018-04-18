from django.urls import path
from django.views.generic import TemplateView
from array import array

from . import views
app_name = 'haipumpfinder'
urlpatterns = [
    path(r'what-the-hai', TemplateView.as_view(template_name="haipumpfinder/what-the-hai.html")),
     path(r'hai-in-the-news', TemplateView.as_view(template_name="haipumpfinder/news.html")),
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    #path('', views.IndexView.as_view(), name='what-the-hai'),
    
    #path('<int:question_id>/vote/', views.vote, name='vote'),
]