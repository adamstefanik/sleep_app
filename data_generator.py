import random
from datetime import datetime

recommended_sleep = 8.5
sleep_efficiency = random.randint(80, 100)
deep_sleep = random.randint(20, 25)  # %
rem_sleep = random.randint(20, 25)  # %

bed_time_start = random.randint(21, 23)
bed_time_end = bed_time_start + random.randint(7, 9)
# adjust if number exceeds 24
if bed_time_end >= 24:
    bed_time_end -= 24

# calculates sleep duration
if bed_time_end >= bed_time_start:
    sleep_duration = bed_time_end - bed_time_start
else:
    sleep_duration = (24 - bed_time_start) + bed_time_end

# formula
sleep_index = (
    sleep_duration / recommended_sleep
    + sleep_efficiency / 100
    + deep_sleep / 100
    + rem_sleep / 100
) * 37

# more values for the app (they are just generated - can't use formula)
resting_hr = random.randint(45, 62)
avg_hrv = random.randint(20, 55)
avg_hr = random.randint(55, 70)
sleep_cycles = random.randint(4, 6)
