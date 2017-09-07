from django.conf.urls import url # URL function
from . import views # views from blog application


urlpatterns = [
    url(r'^$', views.post_list, name='post_list'), # post_list view
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'), # post_detail view
    url(r'^post/new/$', views.post_new, name='post_new'), # post_new view
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'), # post_edit view
    url(r'^draft/$', views.post_draft_list, name='post_draft_list'), # post_draft_list view
    url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'), # post_publish view
    url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'), # post_remove view
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'), # add_comment_to_post view
    url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'), # comment_approve view
    url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'), # comment_remove view
]
