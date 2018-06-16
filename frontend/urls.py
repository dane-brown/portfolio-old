from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.index ),
    url('^projects/$', views.projects),
    url(r'^contact/$', views.contact, name='contact'),
]
