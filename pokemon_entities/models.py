from django.db import models  # noqa F401
from django.utils.timezone import now


class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    image = models.FileField(verbose_name='Image', upload_to='images', blank=True)

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    latitude = models.FloatField(verbose_name='Lat')
    longitude = models.FloatField(verbose_name='Lon')
    pokemon = models.ForeignKey(Pokemon, on_delete=models.PROTECT)
    appeared_at = models.DateTimeField(verbose_name='Appeared at', default=now)
    disappeared_at = models.DateTimeField(verbose_name='Disappeared at', default=now)

    level = models.IntegerField(verbose_name='Level', blank=False)
    health = models.IntegerField(verbose_name='Health', blank=False)
    strength = models.IntegerField(verbose_name='Strength', blank=False)
    defence = models.IntegerField(verbose_name='Defence', blank=False)
    stamina = models.IntegerField(verbose_name='Stamina', blank=False)
