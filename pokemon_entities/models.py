from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    image = models.FileField(verbose_name='Image', upload_to='images', blank=True)

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    latitude = models.FloatField(verbose_name='Lat')
    longitude = models.FloatField(verbose_name='Lon')