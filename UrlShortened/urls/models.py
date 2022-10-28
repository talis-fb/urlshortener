from django.db import models

class User(models.Model):
    user_id = models.TextField()

class Url(models.Model):
    url_id = models.TextField()
    created_at = models.IntegerField()
    original_url = models.TextField()
    hash = models.TextField()
    owner = models.TextField()
    # owner = models.ForeignKey(User, on_delete=models.CASCADE)

