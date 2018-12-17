from django.conf.urls import url
from sample_app import views

urlpatterns = [
    url(r'^index/$', views.index),
]
