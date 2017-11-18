from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200) #길이가 정해져있는 글쓰는 란
    text = models.TextField() #제한없는 글
    created_date = models.DateTimeField(
            default=timezone.now) #time존의 시간을 가져옴
    published_date = models.DateTimeField(
            blank=True, null=True) 

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
