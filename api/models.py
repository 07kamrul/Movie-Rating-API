from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.

#Users Model Here
class UserInfo(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    password = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


#Movies Model Here
class Movie(models.Model):
    RATING_STATUS = (
        ('PG', 'PG'),
        ('R', 'R')
    )
    name = models.CharField(max_length=200, null=True, blank=True)
    genre = models.CharField(max_length=200, null=True, blank=True)
    release_date = models.DateField(auto_now_add=False, auto_now=False, null=True, blank=True)
    movie_rating = models.CharField(max_length=200, null=True, choices=RATING_STATUS)

    def __str__(self):
        return self.name

    #Average rating calculation in a movie
    def avg_ratings(self):
        sum = 0
        ratings = Rating.objects.filter(movie_id=self)
        for rate in ratings:
            sum += rate.rating

        if len(ratings) >= 0:
            avg = sum / len(ratings)
            avg_value = '{:.1f}'.format(avg)

            return avg_value

        else:
            return 0


#Ratings model here
class Rating(models.Model):
    user_id = models.ForeignKey(UserInfo, on_delete= models.CASCADE)
    movie_id = models.ForeignKey(Movie, on_delete= models.CASCADE)
    rating = models.DecimalField(validators=[MinValueValidator(0),MaxValueValidator(5)], max_digits=2, decimal_places=1)

    class Meta:
        unique_together = (('user_id','movie_id'),)
        index_together = (('user_id', 'movie_id'),)