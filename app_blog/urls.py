from django.conf.urls import url
from . import views
from django.views.static import serve
from django.conf import settings


app_name = 'app_blog'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),#每篇文章的地址
	url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
	url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category'),
	url(r'^uploadimg/',views.upload_image),
	url(r'^media/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),
	]