from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from .models import User


@receiver(post_save, sender=User)
def org_creation(sender, instance, created, **kwargs):
    pass