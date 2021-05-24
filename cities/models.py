from django.db import models

__all__ = (
    'City',
)


class City(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Місто')

    class Meta:
        verbose_name = 'Місто'
        verbose_name_plural = 'Міста'
        ordering = ('name',)

    def __str__(self):
        return self.name

    def __str__(self):
        return self.name
