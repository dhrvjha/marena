from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(default='default_profile_image.jpg', upload_to='proflie_pics')

    def __str__(self):
        return f'{ self.user.username } profile'
    
    def save(self):
        super().save()

        img = Image.open(self.profile_image.path)

        if img.height >300 or img.width >300:
            constraint = (300,300)
            
            img.thumbnail(constraint)
            img.save(self.profile_image.path)