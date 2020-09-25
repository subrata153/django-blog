from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^manager/list/$', views.manager_list, name='manager_list'),
]