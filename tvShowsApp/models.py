from django.db import models
from django.db.models.base import Model


class TvShowManger(models.Manager):
    def i_am_the_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['tt']) < 2:
            errors["titlenameRequired"] = "Title name must be aleast 2 characters long"
        if len(postData['net']) < 3:
            errors["networknameRequired"] = "Network name should be at least 3 characters long"
        if len(postData['desc']) < 10:
            errors["descriptionRequired"] = "Description should be at least 10 characters long"
        return errors



# Create your models here.
class TvShows(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = TvShowManger()

    def __str__(self):
        return f"<TvShows object: {self.title} ({self.id})>"