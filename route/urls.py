from django.urls import path
from .import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('project', views.project, name='project'),
    path('contact', views.contact, name='contact'),
    path('project_details', views.project_details, name='project_details'),
]