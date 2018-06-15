from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index ),
    path('projects/', views.projects),
    path('contact/', views.contact),

    url('process-contact-form/', views.process_form)
]
