from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=255, default="")
    image = models.FileField(default="")
    category = models.CharField(max_length=255, default="")
    description = models.TextField()

    def __str__(self):
        return self.name
