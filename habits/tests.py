from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User


# Create your tests here.


class HabitTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            email='nastya2360@mail.ru',
        )

        self.habit = Habit.objects.create(
            owner=self.owner,
            related_habit=None,
            place='дом',
            time='00:10:30',
            action='медитация',
            is_pleasant=False,
            time_to_complete='00:00:50',
            periodicity='1 00:00:00',
        )

        self.client.force_authenticate(owner=self.user)

    def test_habit_list(self):
        response = self.client.get(
            reverse('habits:list-create')
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json()['results'],
            [
                {
                    "id": self.habit.pk,
                    "owner": self.user.id,
                    "related_habit": self.habit.related_habit,
                    "place": self.habit.place,
                    'time': self.habit.time_to_act,
                    "action": self.habit.action,
                    "is_pleasant": self.habit.is_pleasant,
                    "periodicity": self.habit.frequency,
                    "reward": self.habit.reward,
                    "time_to_complete": self.habit.time_to_complete,
                    "is_public": self.habit.is_public

                }
            ]
        )

    def test_create_habit(self):
        data = {
            "id": self.habit.pk,
            "owner": self.user.id,
            "time": '00:09:00',
            "action": 'проснуться',
            "is_pleasant": False,
            "reward": 'шоколадка',
            "time_to_complete": "00:02:00",
            "periodicity": '1 00:00:00',
        }

        response = self.client.post(
            reverse("habits:list-create"),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertTrue(
            Habit.objects.all().exists()
        )

    def test_delete_habit(self):
        response = self.client.delete(
            reverse('habits:habits', args=[self.habit.pk]),
        )

        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )

    def test_update_habit(self):
        update_data = {
            "id": self.habit.pk,
            "owner": self.user.id,
            "time": '00:08:00',
            "action": 'проснуться раньше',
            "is_pleasant": False,
            "reward": 'две шоколадки',
            "time_to_complete": "00:02:00",
            "periodicity": '1 00:00:00',
        }

        response = self.client.put(
            reverse("habits:habits", args=[self.habit.pk]),
            data=update_data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_retrieve_habit(self):
        response = self.client.get(
            reverse('habits:habits', args=[self.habit.pk])
        )

        self.assertEqual(response.status_code,
                         status.HTTP_200_OK)