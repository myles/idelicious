import md5

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import settings
from django.http import HttpResponseRedirect, Http404

from delicious import Delicious

delicious = Delicious(settings.DELICIOUS_API_URL)

def index(request):
	hotlist = delicious.get_hotlist()
	context = {
		'links': hotlist,
	}
	return render_to_response('index.html', context, context_instance=RequestContext(request))

def tag_cloud(request):
	context = {}
	return render_to_response('tag_cloud.html', context, context_instance=RequestContext(request))

def tag(request, tag):
	links = delicious.get_recent_by_tag(tag)
	tags = tag.split("+")
	context = {
		'links': links,
		'tags': tags,
	}
	return render_to_response('tag.html', context, context_instance=RequestContext(request))

def popular(request):
	links = delicious.get_popular()
	context = {
		'links': links,
	}
	return render_to_response('popular.html', context, context_instance=RequestContext(request))

def popular_tag(request, tag):
	tags = tag.split("+")
	links = delicious.get_popular_by_tag(tags[0])
	context = {
		'links': links,
		'tag': tags[0]
	}
	return render_to_response('popular_tag.html', context, context_instance=RequestContext(request))

def user(request, username):
	links = delicious.get_user(username)
	context = {
		'links': links,
		'user': username,
	}
	return render_to_response('user.html', context, context_instance=RequestContext(request))

def user_tag(request, username, tag):
	tags = tag.split("+")
	links = delicious.get_user(username)
	context = {
		'links': links,
		'user': username,
		'tags': tags
	}
	return render_to_response('user_tag.html', context, context_instance=RequestContext(request))

def url(request, url):
	url = delicious.get_url(url)
	if len(url) == 0:
		return Http404
	
	context = {
		'url': url,
		'main_url': url[0]
	}
	return render_to_response('url.html', context, context_instance=RequestContext(request))

def url_get(request):
	url = request.GET.get('url', None)
	if url:
		url_md5 = md5.new(url).hexdigest()
		return HttpResponseRedirect('/url/%s/' % url_md5)
	
	context = {}
	return render_to_response('url_get.html', context, context_instance=RequestContext(request))