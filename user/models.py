from django.db import models
from django.contrib.auth.models import User

class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(default='default_profile_image.jpg', upload_to='proflie_pics')

    def __str__(self):
        return f'{ self.user.username } profile'
    
