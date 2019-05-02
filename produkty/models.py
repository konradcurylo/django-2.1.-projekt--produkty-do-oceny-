from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Towary(models.Model):
    title = models.CharField(max_length=250)
    date = models.DateTimeField(default=timezone.now)
    body = models.TextField()
    url = models.TextField()
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='images/')
    votes_total = models.IntegerField(default=1)
    hunt_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def date_pretty(self):
        return self.date.strftime('%b %e %Y')
