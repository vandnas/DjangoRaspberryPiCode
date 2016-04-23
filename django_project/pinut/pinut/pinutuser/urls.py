from django.conf.urls import url
from django.contrib import admin
admin.autodiscover()

from . import views

urlpatterns = [
    url(r'^pinutuserintro/$', 'pinutuser.views.userintro'),
    url(r'^pinutuserinfo/$', 'pinutuser.views.userinfo'),
    url(r'^pinutconnectioninfo/$', 'pinutuser.views.connectioninfo'),
    url(r'^pinutfeedback/$', 'pinutuser.views.feedback'),
    #url(r'^$', views.index, name='index'),
]
