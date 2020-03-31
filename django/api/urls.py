from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api import views
from views import Start,Stop
from django.conf.urls import include

urlpatterns = [
	url(r'^start/$', Start),
	url(r'^stop/$', Stop),
    url(r'^replay/$', views.ReplayList.as_view()),
    url(r'^replay/(?P<pk>[0-9]+)/$', views.ReplayDetail.as_view()),
    url(r'^features/$', views.FeaturesList.as_view()),
    url(r'^features/(?P<pk>[0-9]+)/$', views.FeaturesDetail.as_view()),
	url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]
urlpatterns = format_suffix_patterns(urlpatterns)