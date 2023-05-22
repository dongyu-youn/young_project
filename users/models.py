from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.shortcuts import reverse
import uuid
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from config import settings



# Create your models here.
class User(AbstractUser): 


    
    phone_number = models.CharField(max_length=40, blank=True, null=True, verbose_name='전화번호')
    
   



    

   

   

