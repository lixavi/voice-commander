# calendar_api.py

import requests

class CalendarAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.calendar.com/v1/events"

    def add_event(self, event_details):
        try:
            headers = {"Authorization": f"Bearer {self.api_key}"}
            response = requests.post(self.base_url, headers=headers, json=event_details)
            if response.status_code == 200:
                return "Event added successfully."
            else:
                return "Sorry, unable to add event at the moment."
        except Exception as e:
            return f"An error occurred: {e}"

    def get_events(self, date):
        try:
            params = {"date": date, "apiKey": self.api_key}
            response = requests.get(self.base_url, params=params)
            data = response.json()
            if response.status_code == 200:
                events = data["events"]
                if events:
                    event_list = "\n".join([event["summary"] for event in events])
                    return f"Events for {date}:\n{event_list}"
                else:
                    return f"No events found for {date}."
            else:
                return "Sorry, unable to fetch events at the moment."
        except Exception as e:
            return f"An error occurred: {e}"
