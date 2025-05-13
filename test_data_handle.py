import pytest
from unittest.mock import patch
from datetime import datetime
from data_handle import (
    get_sleep_quality,
    get_sleep_advice,
    process_sleep_data,
    get_random_quote,
)

# Test for get_sleep_quality() with different sleep index values
@pytest.mark.parametrize("index,expected", [
    (85, "Optimal REM Sleep"),
    (70, "Moderate Sleep Quality"),
    (50, "Poor Sleep Detected"),
])
def test_get_sleep_quality(index, expected):
    assert get_sleep_quality(index) == expected

# Test for get_sleep_advice() with different sleep index values
@pytest.mark.parametrize("index,expected", [
    (90, "Your excellent sleep score indicates optimal REM cycles."),
    (80, "You got adequate rest but missed some sleep. Try going to bed earlier tonight."),
    (60, "Your sleep lacked restorative phases. Avoid screens before bed and reduce caffeine."),
])
def test_get_sleep_advice(index, expected):
    assert get_sleep_advice(index) == expected

# Test for process_sleep_data() with a valid mock data structure
def test_process_sleep_data_valid():
    # Mock sleep and heart rate data
    mock_data = {
        "data": {
            "metric_data": [
                {
                    "type": "sleep",
                    "object": {
                        "details": {
                            "quick_metrics": [
                                {"type": "sleep_index", "value": 88},
                                {"type": "avg_hrv", "value": 45},
                            ],
                            "bedtime_start": 1700000000,
                            "bedtime_end": 1700003600,
                            "sleep_duration": 3600,
                            "sleep_graph": {"data": [1, 2, 3, 4]},
                        }
                    }
                },
                {
                    "type": "night_rhr",
                    "object": {
                        "values": [{"value": 55}]
                    }
                }
            ]
        }
    }

    # Process the data and assert expected values
    result = process_sleep_data(mock_data)
    assert result["sleep_index"] == 88
    assert result["bedtime_start"] == datetime.fromtimestamp(1700000000).strftime("%H:%M")
    assert result["bedtime_end"] == datetime.fromtimestamp(1700003600).strftime("%H:%M")
    assert result["sleep_duration"] == 3600
    assert result["sleep_cycles"] == 4
    assert result["resting_hr"] == 55
    assert result["avg_hrv"] == 45
    assert result["sleep_quality"] == "Optimal REM Sleep"
    assert "sleep_advice" in result

# Test for get_random_quote() using a mocked version of load_quotes()
@patch("data_handle.load_quotes", return_value=[{"quote": "Stay strong!", "author": "Coach"}])
def test_get_random_quote(mocked_quotes):
    result = get_random_quote()
    assert "Stay strong!" in result
    assert "Coach" in result
