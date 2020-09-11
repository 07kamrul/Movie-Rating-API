from rest_framework import serializers

from .models import *

#User Serializer Here
class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ['id','name','phone','password','email']


#Movie Serializer Here
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id','name','genre','movie_rating','release_date']


#Ratings Serializer Here
class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id','user_id','movie_id','rating']


#Search Serializer Here
class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id','name','genre','movie_rating','release_date','avg_ratings']


