from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Games(models.Model):
    """
    Game model
    """

    # Fields
    name = models.CharField(
        max_length=20, help_text="Enter field documentation")
    repository = models.URLField()
    developer = models.ForeignKey('Developer', on_delete=models.SET_NULL)
    description = models.TextField()

    # Metadata

    class Meta:
        ordering = ["-name", "-developer"]

    def __str__(self):
        return self.name+' '+self.developer.name


class Developer(models.Model):
    """
    Developer model
    """

    # Fields
    name = models.CharField(max_length=20)
    website = models.URLField()

    # Metadata

    class Meta:
        ordering = ["-name"]

    def __str__(self):
        return self.name
