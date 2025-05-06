import time
import json
import random
from datetime import datetime, timedelta
from data_generator import generate_sleep_data


def setup_events_and_run(root, ui):
    ui.home_button.bind("<ButtonRelease-1>", lambda e: last_night_data(ui, root))
    root.mainloop()


def last_night_data(ui, root):
    last_night = datetime.now() - timedelta(days=1)
    go_to_loading_screen(ui, root, last_night)


def go_to_loading_screen(ui, root, date):
    ui.show_frame("loading")
    ui.update_loading_quote(get_random_quote())
    root.update()
    fetch_data(ui, date)


def fetch_data(ui, date):
    try:
        time.sleep(2.5)  # Simulated data fetching
        data = generate_sleep_data(date)

        if not data:
            raise ValueError("No data generated")

        processed_data = process_sleep_data(data)
        ui.setup_data_frame(processed_data["sleep_index"])
        ui.update_data_screen(processed_data)
        ui.show_frame("data")

    except Exception as e:
        ui.update_error_message(str(e))
        ui.show_frame("error")


def process_sleep_data(data):
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

        return {
            "sleep_index": sleep_index,
            "bedtime_start": datetime.fromtimestamp(bedtime_start).strftime("%H:%M"),
            "bedtime_end": datetime.fromtimestamp(bedtime_end).strftime("%H:%M"),
            "sleep_duration": sleep_duration,
            "sleep_cycles": sleep_cycles,
            "resting_hr": resting_hr,
            "avg_hrv": avg_hrv,
            "sleep_quality": get_sleep_quality(sleep_index),
            "sleep_advice": get_sleep_advice(sleep_index),
        }

    except Exception as e:
        raise ValueError(f"Data processing error: {str(e)}")


def get_sleep_quality(sleep_index):
    if sleep_index > 81:
        return "Optimal REM Sleep"
    elif sleep_index > 62:
        return "Moderate Sleep Quality"
    else:
        return "Poor Sleep Detected"


def get_sleep_advice(sleep_index):
    if sleep_index > 84:
        return "Your excellent sleep score indicates optimal REM cycles."
    elif sleep_index > 75:
        return "You got adequate rest but missed some deep sleep. Try going to bed 30 mins earlier tonight."
    else:
        return "Your sleep lacked restorative phases. Avoid screens before bed and reduce caffeine."


def load_quotes():
    try:
        with open("quotes.json", "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return [{"quote": "No quotes available.", "author": "System"}]


def get_random_quote():
    quotes = load_quotes()
    if quotes:
        quote = random.choice(quotes)
        return f"\"{quote['quote']}\" - {quote['author']}"
    return "No quotes available."
