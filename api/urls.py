from django.urls import path, include
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register('movies', MovieViewSet)
router.register('users', UserInfoViewSet)
router.register('ratings', RatingViewSet)
router.register('search', SearchViewSet)

urlpatterns = [
    path('', include(router.urls))
]