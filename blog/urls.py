from django.conf.urls import url # URL function
from . import views # views from blog application


urlpatterns = [
    url(r'^$', views.post_list, name='post_list'), # post_list view
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'), # post_detail view
]
