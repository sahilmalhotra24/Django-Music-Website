from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    # /music/
    url(r'^$', views.index),

    # music/45/
    url(r'^(?P<aid>[0-9]+)/$', views.detail, name='detail'),

    # music/45/fav
     url(r'^(?P<aid>[0-9]+)/fav$', views.fav, name='fav'),
]