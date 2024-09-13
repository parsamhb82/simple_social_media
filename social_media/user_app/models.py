from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    following = models.ManyToManyField(User, symmetrical=False, related_name='followers', blank=True)

    def __str__(self) -> str:
        return self.user.get_full_name()


