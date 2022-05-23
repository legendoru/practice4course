from django.db import models

class Emptys(models.Model):
    name = models.TextField()
    email = models.TextField()
    service = models.TextField()
    time = models.TextField()
    msg = models.TextField()

class Review(models.Model):
    name_reviews = models.TextField()
    email_reviews =models.TextField()
    msg_reviews = models.TextField()