import random
import json
from datetime import datetime, timedelta


def generate_sleep_data(date):
    recommended_sleep = 8.5
    sleep_efficiency = random.randint(80, 100)
    deep_sleep = random.randint(20, 25)  # %
    rem_sleep = random.randint(20, 25)  # %

    # Generate sleep times (hours and minutes)
    bedtime_start_hour = random.randint(21, 23)
    bedtime_start_minute = random.randint(0, 59)
    bedtime_end_hour = bedtime_start_hour + random.randint(7, 9)
    bedtime_end_minute = random.randint(0, 59)

    # Adjust for next day if needed
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

    # Format sleep_duration as "hours:minutes"
    sleep_duration_str = f"{sleep_duration_hours}:{sleep_duration_minutes:02}"

    # Calculate sleep index
    sleep_index = (
        (sleep_duration_hours / recommended_sleep * 0.5)
        + (sleep_efficiency / 100 * 0.3)
        + ((deep_sleep + rem_sleep) / 50 * 0.2)
    ) * 110 - 10
    sleep_index = int(sleep_index)

    resting_hr = random.randint(45, 55)
    avg_hrv = random.randint(20, 55)
    sleep_cycles = random.randint(4, 6)

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
                            "sleep_duration": sleep_duration_str,  # Add sleep_duration in "hours:minutes"
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
                                ]
                                * sleep_cycles
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
