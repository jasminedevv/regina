from django.db import models
from django.contrib.auth.models import User

class Submission(models.Model):
    visible_title = models.TextField(blank=False)
    content = models.TextField(blank=False)
    perp_name = models.TextField(blank=False)
    place = models.TextField(blank=False)
    # should be changed to 'author' if we have time to refactor
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    matches = models.IntegerField(default=0)
    matches_users = models.ManyToManyField(User, related_name='matches_users')
    def update_my_matches(self):

    def __str__(self):
        return self.visible_title
