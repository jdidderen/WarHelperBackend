from django.db import models
from django.conf import settings

class Army(models.Model):
    name = models.CharField(max_length=64)
    image = models.ImageField()

    def __str__(self):
        return '%s' % self.name

    def get_image_url(self):
        if self.image:
            return self.image.url
        else:
            return settings.MEDIA_URL + 'tyranids.jpg'
