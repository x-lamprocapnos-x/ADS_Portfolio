# main/urls.py
from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('projects/', views.projects, name='projects'),
    path('projects/<slug:slug>/', views.project_detail, name='project_detail')
]