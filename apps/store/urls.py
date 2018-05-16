from django.conf.urls import url
from . import views


urlpatterns = [
    url('checkout$', views.checkout),
    url('process$', views.process),
    url(r'^$', views.index),
]