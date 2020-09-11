from rest_framework import viewsets

from .serializers import *

#User View Here
class UserInfoViewSet(viewsets.ModelViewSet):
    serializer_class = UserInfoSerializer
    queryset = UserInfo.objects.all()

#Movie View Here
class MovieViewSet(viewsets.ModelViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()

#Rating View Here
class RatingViewSet(viewsets.ModelViewSet):
    serializer_class = RatingSerializer
    queryset = Rating.objects.all()

#Search View Here
class SearchViewSet(viewsets.ModelViewSet):
    serializer_class = SearchSerializer
    queryset = Movie.objects.all()

