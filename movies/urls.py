from rest_framework import routers
from django.urls import include, re_path
from movies.views import MovieViewSet

router = routers.SimpleRouter()
router.register(r'movies', MovieViewSet, basename='movies')

urlpatterns = [
    re_path(r'', include(router.urls,))

]
