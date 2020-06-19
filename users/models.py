from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    cover_photo = models.ImageField(default='defaultcover.jpg', upload_to='cover_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        cover  = Image.open(self.cover_photo.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

        if cover.height > 700 or cover.width > 1000:
            output_size = (500,900)
            cover.thumnail(output_size)
            cover.save(self.cover_photo.path)
