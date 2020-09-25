from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^contact/add', views.add_contact, name='add_contact'),
    url(r'^panel/contact/list/$', views.contact_list, name='contact_list'),
    url(r'^panel/contact/delete/(?P<pk>\d+)/', views.contact_delete, name='contact_delete'),
]
