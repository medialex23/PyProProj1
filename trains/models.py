from django.core.exceptions import ValidationError
from django.db import models
from cities.models import City


class Train(models.Model):
    name = models.CharField(
        max_length=100, unique=True, verbose_name='Номер потягу')
    from_city = models.ForeignKey(
        City, on_delete=models.CASCADE, verbose_name='Звідки',
        related_name='from_city_set')
    to_city = models.ForeignKey(
        City, on_delete=models.CASCADE, verbose_name='Куди',
        related_name='to_city_set')
    travel_time = models.IntegerField(verbose_name='Час в дорозі')

    class Meta:
        verbose_name = 'Потяг'
        verbose_name_plural = 'Потяги'
        ordering = ['name']

    def __str__(self):
        return self.name

    def clean(self, *args, **kwargs):
        if self.from_city == self.to_city:
            raise ValidationError('Змініть місто прибуття')

        qs = Train.objects.filter(
            from_city=self.from_city, to_city=self.to_city,
            travel_time=self.travel_time).exclude(pk=self.pk)
        # Train == self.__class__
        if qs.exists():
            raise ValidationError('Измените время в пути')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)


class TrainTest(models.Model):
    name = models.CharField(max_length=100, unique=True,
                            verbose_name='Номеру потягу')
    from_city = models.ForeignKey(City, on_delete=models.CASCADE,
                                  verbose_name='Звідки',
                                  related_name='test_from_city_set'
                                  )