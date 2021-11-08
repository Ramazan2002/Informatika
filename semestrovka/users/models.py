from django.db import models
from django.utils.timezone import now

# Create your models here.

class Group(models.Model):
    name = models.CharField(max_length=20, default='user')
    description = models.CharField(max_length=50, default='standard user')

    def __str__(self):
        return self.name


class CustomUser(models.Model):
    login = models.CharField(max_length=20, unique=True, editable=False)
    group = models.ForeignKey(Group, on_delete=models.PROTECT)
    password = models.CharField(max_length=100)
    posts_written = models.IntegerField(default=0)
    last_login = models.DateTimeField(default=now(), editable=False)
    join_date = models.DateTimeField(default=now(), editable=False)

    def __str__(self):
        return self.login


class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True, editable=False)
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=35, blank=True)
    photo = models.ImageField(upload_to='user_avatars/', default='default_avatar/1.png')

    def __str__(self):
        return self.name