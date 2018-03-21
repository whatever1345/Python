from django.conf.urls import url
from . import views

app_name='Question'

urlpatterns = [
    url(r'^$', views.Q, name='Q'),
    url(r'^new/$', views.new, name='new'),
    url(r'^(?P<slug>[-\w]+)/$', views.detail, name='detail'),
]