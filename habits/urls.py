from django.urls import path

from habits.apps import HabitConfig
from habits.views import HabitRetrieveUpdateDestroyAPIView, PublicHabitListAPIView, HabitCreateAPIView

app_name = HabitConfig.name

urlpatterns = [
    path('', HabitCreateAPIView.as_view(), name='list-create'),
    path('<int:pk>/', HabitRetrieveUpdateDestroyAPIView.as_view(), name='habits'),

    path('public_habits/', PublicHabitListAPIView.as_view(), name='public_habits')
]