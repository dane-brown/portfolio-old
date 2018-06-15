from django.db import models

class Testimonial(models.Model):
    full_name = models.CharField(max_length=255, default='Testimonial Full Name')
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.FileField(default="")

    def __str__(self):
        return self.full_name
