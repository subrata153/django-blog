from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^panel/$', views.panel, name='panel'),
    url(r'^login/$', views.admin_login, name='admin_login'),
    url(r'^register/$', views.myRegister, name='myRegister'),
    url(r'^logout/$', views.admin_logout, name='admin_logout'),
    url(r'^panel/settings/$', views.site_settings, name='site_settings'),
    url(r'^panel/about/settings/$', views.about_settings, name='about_settings'),
    url(r'^panel/change/pass/$', views.change_pass, name='change_pass'),
]