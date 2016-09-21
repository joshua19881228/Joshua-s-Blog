from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Profile(models.Model):
    profile_user = models.OneToOneField(User, verbose_name='User')
    profile_level = models.IntegerField('Level', default=0)
    profile_real_name = models.CharField(max_length=32, blank=True, null=True)

    def __unicode__(self):
        return self.profile_user.username

    class Meta:
        verbose_name = 'Profile'
