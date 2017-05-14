from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.chathome),
	url(r'^(?P<user_name>[0-9a-zA-Z]+)/$', views.user_home_page, name='user_home_page'),
]
