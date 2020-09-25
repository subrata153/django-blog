from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^panel/sub_category/list/$', views.subcat_list, name='subcat_list'),
    url(r'^panel/sub_category/add/$', views.subcat_add, name='subcat_add')
]