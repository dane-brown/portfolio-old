from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=255, default='Project Name')
    description = models.TextField()
    project_logo = models.FileField(default="")
    logo_background = models.CharField(max_length=255, default="")
    image = models.FileField(default="")
    url = models.CharField(max_length=255, default="")

    def __str__(self):
        return self.name
