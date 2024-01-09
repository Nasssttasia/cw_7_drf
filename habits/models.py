from django.db import models
from datetime import timedelta

from users.models import User

NULLABLE = {'null': True, 'blank': True}


class Habit(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    place = models.CharField(max_length=300, verbose_name='место', **NULLABLE)
    time = models.TimeField(verbose_name='время', **NULLABLE)
    action = models.CharField(max_length=300, verbose_name='действие')
    is_pleasant = models.BooleanField(verbose_name='признак приятной привычки', **NULLABLE)
    related_habit = models.ForeignKey('Habit', on_delete=models.CASCADE, **NULLABLE, verbose_name='связанная привычка')
    periodicity = models.DurationField(default=timedelta(days=1), verbose_name='периодичность')
    reward = models.CharField(max_length=200, verbose_name='вознаграждение', **NULLABLE)
    time_to_complete = models.DurationField(default=timedelta(seconds=120), verbose_name='время на выполнение', **NULLABLE)
    is_public = models.BooleanField(default=False, verbose_name='признак публичности', **NULLABLE)


    def __str__(self):
        return f'{self.action}'

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'
