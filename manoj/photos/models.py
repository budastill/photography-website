from django.db import models

# Create your models here.
class Photos(models.Model):
  photos_text = models.CharField(max_length=200)
  pub_date = models.CharField(max_lerngth=200)
