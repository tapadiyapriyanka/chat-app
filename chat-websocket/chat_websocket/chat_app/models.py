from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class base(models.Model):
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True

class chatmsgs(base):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    textmsg  = models.TextField()

    def __str__(self):
        return str(self.textmsg)
