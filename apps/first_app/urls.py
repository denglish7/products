from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^logoff/$', views.logoff, name='logoff'),
    url(r'^add_page/$', views.add_page, name='add_page'),
    url(r'^add_product/$', views.add_product, name='add_product'),
    url(r'^wish_items/(?P<id>\d+)$', views.show, name='show_page'),
    url(r'^add_to_list/(?P<id>\d+)$', views.add_to_list, name='add_to_list'),
    url(r'^remove_from_list/(?P<id>\d+)$', views.remove_from_list, name='remove_from_list'),
    url(r'^delete/(?P<id>\d+)$', views.delete, name='delete'),
]
