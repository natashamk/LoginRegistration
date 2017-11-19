from django.conf.urls import url
from . import views
import re 

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process$', views.process),
    url(r'^loginprocess$', views.loginprocess),
    url(r'^success$', views.success),
    url(r'^logout$', views.logout)
]