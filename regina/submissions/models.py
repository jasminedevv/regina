from django.db import models
from django.contrib.auth.models import User

class Submission(models.Model):
    visible_title = models.TextField(blank=False)
    content = models.TextField(blank=False)
    perp_name = models.TextField(blank=False)
    place = models.TextField(blank=False)
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.visible_title
