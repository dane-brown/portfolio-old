from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index ),
    path('projects/', views.projects),
    url(r'^contact/$', views.contact, name='contact'),
]
