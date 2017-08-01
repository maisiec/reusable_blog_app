# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.  
class Post(models.Model):
    """
    Here we'll define our Post model
    """
 
    # author is linked to a registered
    # user, via the User model in the auth app. 
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    views = models.IntegerField(default=0) # record how often post is viewed
    tag = models.CharField(max_length=30, blank=True, null=True)

    image = models.ImageField(upload_to="image", blank=True, null=True)
    
 
    def publish(self):
        self.published_date = timezone.now()
        self.save()
 
    def __unicode__(self):
        return self.title