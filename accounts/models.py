from django.db import models
from django.utils import timezone
from django import forms
from django.urls import reverse

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
   # author = models.ForeignKey(user,
   #                            related_name='blog_post', on_delete=models.CASCADE())
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField( auto_now_add=True )
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length= 10,choices=STATUS_CHOICES,default='draft')

    # def get_absolute_url(self):
    #     return reverse('account:post_detail', args=[self.publish.year
    #                                                 ,self.publish.strftime('%m')
    #                                                 ,self.publish.strftime('%d')])

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title






