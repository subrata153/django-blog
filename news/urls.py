from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^news/(?P<word>.*)/$', views.news_details, name='news_details'),
    url(r'^panel/news/list/$', views.news_list, name='news_list'),
    url(r'^panel/news/add/$', views.news_add, name='news_add'),
    url(r'^panel/news/delete(?P<pk>\d+)/$', views.news_delete, name='news_delete'),
    url(r'^panel/news/edit/(?P<pk>\d+)/$', views.news_edit, name='news_edit'),
    url(r'^panel/trending/add/$', views.trending_add, name='trending_add'),
    url(r'^panel/trending/delete/(?P<pk>\d+)/$', views.del_tredning, name='del_tredning'),
    url(r'^panel/trending/edit/(?P<pk>\d+)/$', views.edit_trending, name='edit_trending'),
]
