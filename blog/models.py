import datetime
from django.utils import timezone
from django.db import models


# Create your models here.

class posts(models.Model):
    title = models.CharField(max_length=50)
    date_posted = models.DateTimeField(auto_now_add=True)
    post_text = models.CharField(max_length=300)
    like = models.IntegerField(default=0)
    comment = models.CharField(null=True, max_length=200,blank=True)
    author = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.title

    def was_publilsed_recently(self):
        return self.date_posted >= timezone.now() - datetime.timedelta(days = 1)
    