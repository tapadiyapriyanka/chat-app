from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
import datetime
from django.forms import TextInput, Textarea
# Create your models here.



class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract=True

class chatmessage(Base):
   username = models.ForeignKey(User,on_delete=models.CASCADE)
   textmsg = models.TextField()


   def get_absolute_url(self):
        return reverse('homepage')

   def __str__(self):
       return str(self.username)
