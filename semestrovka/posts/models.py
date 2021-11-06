from django.db import models
from users.models import CustomUser, UserProfile
from django.utils.timezone import now


class Post(models.Model):
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, editable=False)
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=2500)
    publication_date = models.DateTimeField(default=now(), editable=False)

    def __str__(self):
        return str(self.title)

class ImagesForPost(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts_images/', null=True, blank=True)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    text = models.TextField(max_length=100, null=False, blank=False)
    publication_date = models.DateTimeField(default=now(), editable=False)

    def __str__(self):
        return f"Comment by {self.author.name} on {self.post} at {self.publication_date.strftime('%H:%M %d.%m.%Y')}"