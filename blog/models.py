from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from django.contrib import admin
import datetime
# Create your models here.
class BlogPost(models.Model):
    def __str__(self):
        return self.blog_post
    blog_post = models.TextField('Blog post',max_length=200)
    publisher_name = models.CharField('Publisher name',max_length=200)
    blog_subject = models.CharField('Blog subject',max_length=100)
    
    pub_date = models.DateTimeField('date published')
    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    