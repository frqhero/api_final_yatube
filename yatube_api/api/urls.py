from django.urls import path
from rest_framework import routers
from .views import PostViewSet, GroupViewSet
from django.urls import include

router = routers.SimpleRouter()
router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
