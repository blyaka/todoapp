from django.db import models
from django.urls import reverse
import uuid
from django.contrib.auth.models import AbstractUser
from django.db.models import F

class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    avatar = models.ImageField(verbose_name='avatar', null=True, blank=True, upload_to='profile/')
    #rang = models.IntegerField(default=0)


    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('profile', args=[str(self.id)])

    def get_avatar(self):
        if not self.avatar:
            self.avatar = 'profile/default.png'
        return self.avatar.url






