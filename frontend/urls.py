from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.index, name='index'),
    url('^projects/$', views.projects, name='projects'),
    url(r'^contact/$', views.contact, name='contact'),
]
