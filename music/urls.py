from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    # /music/
    url(r'^$', views.IndexView.as_view(),name= 'index'),

    # music/45/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    #/music/album/add/
    url(r'album/add/$', views.AddCreate.as_view(), name='add-album'),
]