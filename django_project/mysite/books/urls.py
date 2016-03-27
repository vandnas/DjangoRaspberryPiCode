from django.conf.urls import url
from django.contrib import admin
admin.autodiscover()

from . import views

urlpatterns = [
#     url(r'^$', 'views.print1', name='books'),
     	url(r'^$', 'books.views.print1'),
        url(r'^(?P<book_id>[0-9]+)/$', 'books.views.print2'),
        url(r'^register/$', 'books.views.register'),
        url(r'^selectspecificbook/(?P<book_id>[0-9]+)/$', 'books.views.selectspecificbook'),
        url(r'^selectallbooks/$', 'books.views.selectallbooks'),
        url(r'^deletespecificbook/(?P<book_id>[0-9]+)/$', 'books.views.deletespecificbook'),
        url(r'^deleteallbooks/$', 'books.views.deleteallbooks'),

]

