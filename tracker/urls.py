from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^newitem/$', views.create_item, name='newitem'),
    url(r'^(?P<item_id>[0-9]+)', views.detail, name='detail'),
]
