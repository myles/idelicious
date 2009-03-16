from django.conf.urls.defaults import *

urlpatterns = patterns('views',
	(r'^(?P<username>(.*))/(?P<tag>(.*))/$', 'user_tag'),
	(r'^(?P<username>(.*))/$', 'user'),
	(r'^popular/(?P<tag>(.*))/$', 'popular_tag'),
	(r'^popular/$', 'popular'),
	(r'^tag/(?P<tag>(.*))/$', 'tag'),
	(r'^$', 'index'),
)