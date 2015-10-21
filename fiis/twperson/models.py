from django.db import models
from datetime import datetime 
# Create your models here.

class UserTw(models.Model):

    screen_name = models.CharField(u'Screen name', max_length=50)
    screen_id 	= models.CharField(u'Id', max_length=100, blank=True, unique=True)
    description = models.TextField(u'Description', blank=True, null=True)
    timeline 	= models.TextField(u'Timeline', blank=True, null=True)
    created     = models.DateTimeField(u'fecha ingreso', default=datetime.now, blank=True)
    personality = models.TextField(u'Personality', blank=True, null=True)
    challenge   = models.TextField(u'challenge', blank=True, null=True)
    closeness   = models.TextField(u'closeness', blank=True, null=True)
    curiosity   = models.TextField(u'curiosity', blank=True, null=True)
    excitement  = models.TextField(u'excitement', blank=True, null=True)
    harmony     = models.TextField(u'harmony', blank=True, null=True)
    ideal       = models.TextField(u'ideal', blank=True, null=True)
    liberty     = models.TextField(u'liberty', blank=True, null=True)
    love        = models.TextField(u'love', blank=True, null=True)
    practicality = models.TextField(u'practicality', blank=True, null=True)
    selfexpression = models.TextField(u'selfexpression', blank=True, null=True)
    stability = models.TextField(u'stability', blank=True, null=True)
    structure = models.TextField(u'structure', blank=True, null=True)

class Status(models.Model):

    usertw      = models.TextField(u'UserTw', blank=True)
    text        = models.TextField(u'Tweet', blank=True, null=True)
    keywords    = models.TextField(u'Keywords', blank=True, null=True)
    sentiment   = models.TextField(u'Setiment', blank=True, null=True)
    created_tw  = models.DateTimeField(u'fecha tweet', blank=True)
    
