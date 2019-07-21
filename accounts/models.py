from django.db import models
from django.utils import timezone
from django import forms
from django.urls import reverse
from django.contrib.auth.models import User

# # Create your models here.



class books(models.Model):
    name = models.CharField(max_length=100)



class user(models.Model):

        last_name =  models.CharField(max_length=100)
        email = models.EmailField()
        password = models.CharField(max_length=50)

class PublishedManager (models.Manager):
    def get_queryset(self):
        return super(PublishedManager,
                     self).get_queryset().filter(status = 'published')

class Post(models.Model):
    published = PublishedManager()
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250,
                                unique_for_date='publish')
    author = models.ForeignKey(User,
                              related_name='blog_post', on_delete=models.CASCADE,default='10000')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField( auto_now_add=True )
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length= 10,choices=STATUS_CHOICES,default='draft')
    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    class Meta:
        ordering = ('created',)

class Tag(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)








