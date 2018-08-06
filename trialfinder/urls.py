from django.urls import path
from . import views
app_name = "trialfinder"

urlpatterns = [
    path('', views.index, name='index'),
    
]