from datetime import datetime
import os
import dotenv
import requests
from celery import shared_task

from habits.models import Habit

dotenv.load_dotenv()


@shared_task
def check_time_habits():
    datetime_now = datetime.now()
    time_now = datetime_now.strftime("%H:%M:00")
    habits = Habit.objects.filter(time_to_act=time_now)
    for habit in habits:
        data = {
            'chat_id': habit.user.user_telegram_id,
            'text': f"Hello {habit.user.email}\n"
                    f"You need to do {habit.action}\n"
                    f"time to complete - {habit.time_to_complete}"
        }

        requests.post(f"https://api.telegram.org/bot{os.getenv('TG_ACCESS_TOKEN')}/sendMessage", data)
