from django.conf.urls import url
from . import views

app_name = 'articles'

urlpatterns = [
    url(r'^$', views.article_list, name="list"),
    url(r'^create/$', views.article_create, name="create"),
    url(r'^(?P<slug>[\w-]+)/$', views.article_detail, name="detail"),
    url(r'^delete/(?P<title>[\w-]+)/$', views.article_delete, name="delete"),
    url(r'^details/(?P<author>[\w-]+)/$', views.user_detail, name="details"),
]
