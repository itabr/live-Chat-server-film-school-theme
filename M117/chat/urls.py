from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.chathome),
	url(r'^test/$', views.test),
	url(r'^private/(?P<token>[0-9a-zA-Z]+)/(?P<user_name>[0-9a-zA-Z]+)/$', views.privatechat),
	url(r'^(?P<user_name>[0-9a-zA-Z]+)/$', views.user_home_page, name='user_home_page'),
	url(r'^(?P<chatrooms>[0-9a-zA-Z]+)/(?P<user_name>[0-9a-zA-Z]+)/$', views.chatrooms, name='action'),
]
