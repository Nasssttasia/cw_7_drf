from rest_framework import serializers

from habits.models import Habit
from habits.validators import validate_period, validate_time_to_complete, validate_related_fields_habits, \
    validate_reward_fields_habits


class HabitSerializer(serializers.ModelSerializer):
    periodicity = serializers.DurationField(validators=[validate_period])
    time_to_complete = serializers.DurationField(validators=[validate_time_to_complete])

    class Meta:
        model = Habit
        fields = '__all__'
        validators = [validate_related_fields_habits, validate_reward_fields_habits]

