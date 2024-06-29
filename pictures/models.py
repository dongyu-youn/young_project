from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from core.models import TimeStampedModel
from django.urls import reverse

from core import models as core_models



class AbstractItem(core_models.TimeStampedModel):

    """ Abstract Item """

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Mind(AbstractItem):

    """ RoomType Model Definition """

    class Meta:
        verbose_name = "관념"


class Shape(AbstractItem):

    """ Amenity Model Definition """

    class Meta:
        verbose_name_plural = "형태"


class Color(AbstractItem):

    """ Facility Model Definition """

    pass

    class Meta:
        verbose_name_plural = "색깔"


class Other(AbstractItem):

    """ HouseRule Model Definition """

    class Meta:
        verbose_name = "기타"


class SearchHistory(models.Model):
    query = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="ss",  null=True, blank=False
    ) 
    count = models.PositiveIntegerField(default=0)


    def __str__(self):
        return self.query
    



# Create your models here.
class Picture(TimeStampedModel): 

    SEMI_A = "wom"
    SEMI_B = "man"
    SEMI_C = "new"
    SEMI_D = "today"


    SEMI_CHOICES = (
      (SEMI_A, "wom"),
      (SEMI_B, "man"),
      (SEMI_C, "new"),
      (SEMI_D, "today"),
    )

    제목 = models.CharField(max_length=100, null=True,  default = '', verbose_name='제목')
    desc = models.TextField(max_length=300, default = '', null=True, verbose_name='내용')
    image = models.ImageField(blank=True)
    filter = models.CharField(choices=SEMI_CHOICES, default = '', max_length=10, blank=False, null=True)

    
    mind = models.ManyToManyField("Mind", related_name="mind", blank=True)  
    shape = models.ManyToManyField("Shape", related_name="shape", blank=True)
    color = models.ManyToManyField("Color", blank=True)
    other = models.ManyToManyField("Other", blank=True)
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="ㄴ",  null=True, blank=False
    ) 

    


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


class Favorite(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    picture = models.ForeignKey(Picture, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'picture')




