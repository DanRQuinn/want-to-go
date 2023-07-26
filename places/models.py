from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

class Places(models.Model):
  title = models.CharField(max_length=64)
  body = models.TextField(default='1. ')
  author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse('places_detail', args=[str(self.id)])
