from django.db import models

class Lead(models.Model):

    full_name = models.CharField(max_length=255, default='')

    email_address = models.CharField(max_length=255, default='')

    comments = models.TextField()

    def __str__(self):
        return self.full_name
