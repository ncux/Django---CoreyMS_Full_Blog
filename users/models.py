from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.jpg', upload_to='avatars')

    def __str__(self):
        return f'Profile of {self.user.username}'

    def save(self, **kwargs):        # add **kwargs to avoid "user - save() got an unexpected keyword argument 'force_insert'"
        super().save()

        image = Image.open(self.avatar.path)
        if image.height > 300 or image.width > 300:
            output_size = (300, 300)
            image.thumbnail(output_size)
            image.save(self.avatar.path)




