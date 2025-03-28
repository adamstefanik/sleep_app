import json
import random
import time
import tkinter as tk
from datetime import datetime, timedelta
from gui import SleepTrackerUI
from data_generator import generate_sleep_data


class SleepTrackerApp:
    def __init__(self):
        self.root = tk.Tk()
        self.ui = SleepTrackerUI(self.root)

        # Bind UI events
        self.ui.home_button.bind("<ButtonRelease-1>", lambda e: self.last_night_data())

        # Start the app
        self.root.mainloop()

    def last_night_data(self):
        last_night = datetime.now() - timedelta(days=1)
        self.go_to_loading_screen(last_night)

    def go_to_loading_screen(self, date):
        self.ui.show_frame("loading")
        self.ui.update_loading_quote(self.get_random_quote())
        self.root.update()  # Force UI update before long operation
        self.fetch_data(date)

    def fetch_data(self, date):
        try:
            time.sleep(2.5)  # Simulate data fetching delay
            data = generate_sleep_data(date)

            if not data:
                raise ValueError("No data generated")

            self.process_sleep_data(data, date)
            self.ui.show_frame("data")

        except Exception as e:
            self.ui.update_error_message(str(e))
            self.ui.show_frame("error")

    def process_sleep_data(self, data, date):
        try:
            sleep_data = next(
                metric["object"]
                for metric in data["data"]["metric_data"]
                if metric["type"] == "sleep"
            )

            night_rhr_data = next(
                metric["object"]
                for metric in data["data"]["metric_data"]
                if metric["type"] == "night_rhr"
            )

            # Extract all required values
            sleep_index = next(
                metric["value"]
                for metric in sleep_data["details"]["quick_metrics"]
                if metric["type"] == "sleep_index"
            )
            bedtime_start = sleep_data["details"]["bedtime_start"]
            bedtime_end = sleep_data["details"]["bedtime_end"]
            sleep_duration = sleep_data["details"]["sleep_duration"]
            sleep_cycles = len(sleep_data["details"]["sleep_graph"]["data"])
            resting_hr = night_rhr_data["values"][0]["value"]
            avg_hrv = next(
                metric["value"]
                for metric in sleep_data["details"]["quick_metrics"]
                if metric["type"] == "avg_hrv"
            )

            # Prepare data for UI
            processed_data = {
                "sleep_index": sleep_index,
                "bedtime_start": datetime.fromtimestamp(bedtime_start).strftime(
                    "%H:%M"
                ),
                "bedtime_end": datetime.fromtimestamp(bedtime_end).strftime("%H:%M"),
                "sleep_duration": sleep_duration,
                "sleep_cycles": sleep_cycles,
                "resting_hr": resting_hr,
                "avg_hrv": avg_hrv,
                "sleep_quality": self.get_sleep_quality(sleep_index),
                "sleep_advice": self.get_sleep_advice(sleep_index),
            }

            # Update UI
            self.ui.setup_data_frame(sleep_index)
            self.ui.update_data_screen(processed_data)

        except Exception as e:
            self.ui.update_error_message(f"Data processing error: {str(e)}")
            self.ui.show_frame("error")

    def get_sleep_quality(self, sleep_index):
        if sleep_index > 81:
            return "Optimal REM Sleep"
        elif sleep_index > 62:
            return "Moderate Sleep Quality"
        else:
            return "Poor Sleep Detected"

    def get_sleep_advice(self, sleep_index):
        if sleep_index > 84:
            return "Your excellent sleep score indicates optimal REM cycles."
        elif sleep_index > 75:
            return "You got adequate rest but missed some deep sleep. Try going to bed 30 mins earlier tonight."
        else:
            return "Your sleep lacked restorative phases. Avoid screens before bed and reduce caffeine."

    def load_quotes(self):
        try:
            with open("quotes.json", "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return [{"quote": "No quotes available.", "author": "System"}]

    def get_random_quote(self):
        quotes = self.load_quotes()
        if quotes:
            quote = random.choice(quotes)
            return f"\"{quote['quote']}\" - {quote['author']}"
        return "No quotes available."


if __name__ == "__main__":
    app = SleepTrackerApp()
