from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from core.models import TimeStampedModel
from django.urls import reverse

# Create your models here.
class Picture(TimeStampedModel): 
    제목 = models.CharField(max_length=100, null=True,  default = '', verbose_name='제목')
    desc = models.TextField(max_length=300, default = '', null=True, verbose_name='내용')
    image = models.ImageField(blank=True)
    
    class Meta:
        ordering = ["-created"] 
        
    @property
    def get_photo_url(self): 
      if self.image:
          return self.image.url 
      else:
          return "/static/images/user.jpg"

    # def get_absolute_url(self):
    #     return reverse("project:detail", kwargs={"pk": self.pk})



