
from django.db import models
from accounts.models import User



class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'


class Video(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    thumbnail = models.ImageField(upload_to="thumbnail")
    video = models.FileField(upload_to='videos_uploaded', null=True,)
    category = models.ManyToManyField(
        Category, default=None, related_name='category', blank=False,)

    views = models.ManyToManyField(User, default=None, related_name='views', blank=False)
    updated = models.DateTimeField(auto_now=True, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.title}'

    def getID(self):
        return self.id

    class Meta:
        ordering = ['-created']


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Video, on_delete=models.CASCADE)
    body = models.TextField(max_length=300)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.pk)

    class Meta:
        ordering = ['-created']
