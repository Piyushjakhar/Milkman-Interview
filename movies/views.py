from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from movies.models import Movies
from movies.serializers import MovieSerializer


# Create your views here.
class MovieViewSet(viewsets.ViewSet):

    @action(methods=['GET'], detail=False, url_path='list')
    def get_movie_list(self, request):
        movie_list = Movies.objects.filter(is_active=True)
        serializer = MovieSerializer(movie_list, many=True)
        return Response(data=serializer.data, status=HTTP_200_OK)
