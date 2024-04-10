from django.db import models
import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class TodoList(models.Model):
    title=models.CharField(max_length=200)
    status=models.BooleanField(default=False)
    created_at=models.DateField(default=datetime.datetime.today().date())

    def __str__(self):
        return self.title
    
class WebsiteViews(models.Model):
    total_views=models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.total_views

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)



