from django.db import models

class Crossing(models.Model):
    name = models.TextField(null=False)
    jurisdiction = models.TextField(null=True)
    address = models.TextField(null=True)
    lat = models.FloatField(default=0, null=False)
    lon = models.FloatField(default=0, null=False)
    comment = models.TextField(null=True)
    status = models.IntegerField(default=0, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
class Camera(models.Model):
    unique_id = models.TextField(null=False)
    name = models.TextField(null=True)
    address = models.TextField(null = False)
    lat = models.FloatField(default=0, null=False)
    lon = models.FloatField(default=0, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Image(models.Model):
    camera_id = models.IntegerField(null=False)
    name = models.TextField(null=False)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(auto_now=True)