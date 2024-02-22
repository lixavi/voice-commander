# reminder.py

import datetime

class Reminder:
    def __init__(self):
        self.reminders = []

    def set_reminder(self, time, message):
        try:
            reminder_time = datetime.datetime.strptime(time, "%Y-%m-%d %H:%M")
            self.reminders.append((reminder_time, message))
            return "Reminder set successfully."
        except ValueError:
            return "Invalid time format. Please use YYYY-MM-DD HH:MM format for the reminder."
        except Exception as e:
            return f"An error occurred: {e}"
