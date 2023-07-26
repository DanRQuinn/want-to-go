from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

class Review(models.Model):
  title = models.CharField(max_length=64, default='review')
  body = models.TextField(default='review')
  author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
  
  def __str__(self):
    return self.title
  
  def get_absolute_url(self):
    return reverse('review_detail', args=[str(self.id)])
