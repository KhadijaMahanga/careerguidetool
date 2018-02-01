from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^school/(?P<schoolcode>[\w.-]+)/$', views.school, name='school'),
    url(r'^subjects/a-level', views.alevel_subjects, name='subjects/a-level'),
    url(r'^subjects/o-level', views.olevel_subjects, name='subjects/o-level')
    ]
