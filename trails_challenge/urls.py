from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers

from challenge import views


router = routers.DefaultRouter()
router.register(r'groups', views.GroupViewSet)
router.register(r'techniques', views.TechniqueViewSet)
router.register(r'patrols', views.PatrolViewSet)
router.register(r'tests', views.TestViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'trails_challenge.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/v1/', include(router.urls)),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', 'rest_framework_jwt.views.obtain_jwt_token'),
)
