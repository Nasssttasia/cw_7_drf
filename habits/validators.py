from rest_framework.exceptions import ValidationError

from habits.models import Habit


def validate_related_fields_habits(value):
    if value.get('reward') and value.get('is_pleasant'):
        raise ValidationError('Pleasant habit cant has a reward')
    if value.get('related_habit') and value.get('is_pleasant'):
        raise ValidationError('Pleasant habit cant has a related habit')
    if value.get('related_habit'):
        habit = Habit.objects.get(pk=value.get('related_habit').id)
        print(habit)
        if not habit.is_pleasant:
            raise ValidationError('Related habit has to be a pleasant habit')


def validate_reward_fields_habits(value):
    if sum([bool(value.get('related_habit')), bool(value.get('reward')), bool(value.get('is_pleasant'))]) < 1:
        raise ValidationError('You need to choose the reward or related_habit for the unpleasant habit')


def validate_period(value):
    if value.days >= 8:
        raise ValidationError('Period should be less then 7')


def validate_time_to_complete(value):
    if value.total_seconds() > 120:
        raise ValidationError('Time to complete a habit has to be less then 120 seconds')