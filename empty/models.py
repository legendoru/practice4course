from django.db import models

class Emptys(models.Model):
    name = models.TextField()
    email = models.TextField()
    service = models.TextField()
    time = models.TextField()
    msg = models.TextField()
