from django.conf.urls import url # URL function
from . import views # views from blog application


urlpatterns = [
    url(r'^$', views.post_list, name='post_list'), # post_list view
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'), # post_detail view
    url(r'^post/new/$', views.post_new, name='post_new'), #post_new view
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
]
