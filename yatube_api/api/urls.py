from django.urls import path
from rest_framework import routers
from .views import PostViewSet
from django.urls import include

router = routers.SimpleRouter()
router.register('posts', PostViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
]
