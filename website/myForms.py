from django.db import models


class Post(models.Model):
    name = models.TextField(blank=False, null=False)
    email = models.EmailField(blank=False, null=False, unique=False)
    message = models.TextField(blank=False, null=False)
    time = models.DateTimeField(auto_now_add=True)
    ipaddress = models.GenericIPAddressField(auto_created=True, null=True)


class Newsletters(models.Model):
    email = models.EmailField(blank=False, null=False, unique=True)
    time = models.DateTimeField(auto_now_add=True)
    ipaddress = models.GenericIPAddressField(auto_created=True, null=True)