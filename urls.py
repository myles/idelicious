from django.conf.urls.defaults import *

urlpatterns = patterns('views',
	(r'^url/(?P<url>(.*))/$', 'url'),
	(r'^url/$', 'url_get'),
	(r'^popular/(?P<tag>(.*))/$', 'popular_tag'),
	(r'^popular/$', 'popular'),
	(r'^tag/(?P<tag>(.*))/$', 'tag'),
	(r'^tag/$', 'tag_cloud'),
	(r'^(?P<username>(.*))/(?P<tag>(.*))/$', 'user_tag'),
	(r'^(?P<username>(.*))/$', 'user'),
	(r'^$', 'index'),
)