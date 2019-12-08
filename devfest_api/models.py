from django.db import models

# Create your models here.
class Hall(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=150)
  capacity = models.IntegerField()

class Speaker(models.Model):
  id = models.AutoField(primary_key=True)
  first_name = models.CharField(max_length=150)
  last_name = models.CharField(max_length=150)
  photo = models.ImageField(upload_to='uploads')
  job = models.CharField(max_length=150)
  tags = models.TextField()
  github_url = models.URLField(blank=True,null=True)
  twitter_url = models.URLField(blank=True,null=True)
  linkedin_url = models.URLField(blank=True,null=True)

class Attendee(models.Model):
  id = models.AutoField(primary_key=True)
  first_name = models.CharField(max_length=150)
  last_name = models.CharField(max_length=150)
  email = models.EmailField(max_length=150)
  id_google_login = models.CharField(max_length=150,blank=True, null=True)

class Conference(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.TextField()
  start_at = models.TimeField()
  ends_at = models.TimeField()
  speaker = models.ManyToManyField(Speaker)
  attendees = models.ManyToManyField(Attendee)

