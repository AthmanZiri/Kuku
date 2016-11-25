from django.conf.urls import url, include
from django.views.generic import ListView,DetailView
from Adds.models import Adds
from . import views

urlpatterns=[
     url(r'^$', ListView.as_view(queryset=Adds.objects.all().order_by("-date")[:25], template_name="Adds/index.html")),
     url(r'^(?P<pk>\d+)$', DetailView.as_view(model= Adds,template_name='Adds/detail.html')),
     #url(r'^(?P<pk>[0-9]+)/Adds/$', views.get_form, name='get_form'),
     url(r'^about/$', views.about, name='about'),
     url(r'^map/$', views.map, name='map'),
     url(r'^detail/$', views.detail, name='detail'),
     url(r'^login/$', views.login, name='login'),
     url(r'^blog/$', views.blog, name='blog'),
    ]