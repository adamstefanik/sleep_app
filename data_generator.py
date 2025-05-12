import random
from datetime import datetime, timedelta


# Generates simulated sleep data for a given date
def generate_sleep_data(date):
    recommended_sleep = 8.5
    sleep_efficiency = random.randint(80, 100)
    deep_sleep = random.randint(20, 25)  # %
    rem_sleep = random.randint(20, 25)   # %

    # Generate random bedtime start and end times
    bedtime_start_hour = random.randint(21, 23)
    bedtime_start_minute = random.randint(0, 59)
    bedtime_end_hour = bedtime_start_hour + random.randint(7, 9)
    bedtime_end_minute = random.randint(0, 59)

    # Adjust the end date if sleep ends after midnight
    if bedtime_end_hour >= 24:
        bedtime_end_hour -= 24
        end_date = date + timedelta(days=1)
    else:
        end_date = date

    # Convert to datetime objects
    bedtime_start = datetime.combine(date, datetime.min.time()).replace(
        hour=bedtime_start_hour, minute=bedtime_start_minute
    )
    bedtime_end = datetime.combine(end_date, datetime.min.time()).replace(
        hour=bedtime_end_hour, minute=bedtime_end_minute
    )

    # Calculate duration in hours and minutes
    sleep_duration_seconds = (bedtime_end - bedtime_start).total_seconds()
    sleep_duration_hours = int(sleep_duration_seconds // 3600)
    sleep_duration_minutes = int((sleep_duration_seconds % 3600) // 60)

    # Format sleep duration as string "H:MM"
    sleep_duration_str = f"{sleep_duration_hours}:{sleep_duration_minutes:02}"

    # Creates sleep index based on duration, efficiency, and sleep stages
    sleep_index = (
        (sleep_duration_hours / recommended_sleep * 0.5)
        + (sleep_efficiency / 100 * 0.3)
        + ((deep_sleep + rem_sleep) / 50 * 0.2)
    ) * 110 - 10
    sleep_index = int(sleep_index)

    # Simulated physiological metrics
    resting_hr = random.randint(45, 55)
    avg_hrv = random.randint(20, 55)
    sleep_cycles = random.randint(4, 6)

    # Construct the JSON-like data structure representing sleep metrics
    json_data = {
        "data": {
            "metric_data": [
                {
                    "type": "sleep",
                    "object": {
                        "day_start_timestamp": bedtime_end.timestamp(),
                        "details": {
                            "bedtime_start": bedtime_start.timestamp(),
                            "bedtime_end": bedtime_end.timestamp(),
                            "sleep_duration": sleep_duration_str,
                            "quick_metrics": [
                                {"type": "sleep_index", "value": sleep_index},
                                {"type": "avg_hrv", "value": avg_hrv},
                            ],
                            "sleep_graph": {
                                "data": [
                                    {
                                        "start": bedtime_start.timestamp(),
                                        "end": bedtime_end.timestamp(),
                                    }
                                ] * sleep_cycles
                            },
                        },
                    },
                },
                {
                    "type": "night_rhr",
                    "object": {
                        "day_start_timestamp": bedtime_end.timestamp(),
                        "values": [{"value": resting_hr}],
                    },
                },
            ]
        }
    }

    return json_data
