from django.conf.urls import url, include
from django.views.generic import ListView,DetailView
from Adds.models import Adds

urlpatterns=[
     url(r'^$', ListView.as_view(queryset=Adds.objects.all().order_by("-date")[:25], template_name="Adds/base.html")),
     url(r'^Add/(?P<pk>\d+)$', DetailView.as_view(model= Adds,template_name='Adds/add_detail.html')),
     #url(r'^(?P<pk>[0-9]+)/Adds/$', views.get_form, name='get_form'),
    ]