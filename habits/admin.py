from django.contrib import admin

from habits.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ('reward', 'is_pleasant', 'related_habit', 'owner', 'time_to_complete')