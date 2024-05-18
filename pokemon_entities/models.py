from django.db import models  # noqa F401
from django.utils.timezone import now


class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(verbose_name='Image', upload_to='images', blank=True)
    title_ru = models.CharField(max_length=200, blank=True)
    title_en = models.CharField(max_length=200, blank=True)
    title_jp = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)

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

    def __str__(self):
        return self.pokemon.title + ' ' + str(self.level)