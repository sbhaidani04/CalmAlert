# CalmAlert

### Breathe easy, we’ve got you.

![image](https://github.com/user-attachments/assets/771f43ca-3eac-4238-a016-1fb2f125bcad)

---

## Overview

CalmAlert is a desktop application, currently built with Python’s Tkinter library, designed to manage and monitor stress levels through simulated data. It calculates a stress score based on heart rate (HR) and environmental noise levels (decibels, dB), providing recommendations for managing stress. Eventually, we aim to scale CalmAlert into a smartwatch application.

---

## Features

- **Stress Score Calculation**: Uses heart rate and environmental noise data to compute a real-time stress score.
- **Data Simulation**: Generates heart rate and decibel data through custom functions and Python’s `random` module for testing.
- **Recommendations**: Provides gentle recommendations to help users manage stress based on calculated scores.
- **Built with Tkinter**: Provides a simple and interactive desktop interface.

---

## Technical Details

### Stress Calculation Functions

CalmAlert calculates stress based on two primary metrics: heart rate and environmental noise.

1. **Heart Rate (HR) Stress Level Calculation**

   ```python
   import math

   def hr_stress_level(user_avg_hr, user_cur_hr, k=0.02):
       hr_diff = user_cur_hr - user_avg_hr
       hr_stress = 50 * (1 - math.exp(-k * hr_diff))
       return hr_stress
   ```

   This function computes stress based on the difference between the user’s current and average heart rates, applying an exponential scaling factor.

2. **Decibel (dB) Stress Level Calculation**

   ```python
   def db_stress_level(decibel_value, threshold=70, k=0.07):
       if decibel_value > threshold:
           scaled_stress = 50 * (1 - math.exp(-k * (decibel_value - threshold)))
           return min(scaled_stress, 50)
       else:
           return 0
   ```

   This function calculates stress from environmental noise levels, capping the stress score at 50.

3. **Overall Stress Level Calculation**

   ```python
   def overall_stress_level(user_average_hr, user_current_hr, db_value, threshold=70):
       hr_stress = hr_stress_level(user_average_hr, user_current_hr)
       db_stress = db_stress_level(db_value)
       stress_level = hr_stress + db_stress
       return stress_level
   ```

### Data Simulation Functions

To mimic real-world variations in heart rate and noise, we use the following simulation functions:

- **Normal Decibel Variation** (targets around 60 dB)
- **Stressed Decibel Variation** (targets around 90 dB)

Example implementations:

```python
import random

# Normal decibel variation
def normal_decibel_variation(cur_value, target=60, max_change=3):
    if cur_value < target:
        change = random.uniform(0, max_change)
    elif cur_value > target:
        change = -random.uniform(0, max_change)
    else:
        change = random.uniform(-max_change, max_change)

    next_db = cur_value + change
    return max(40, min(next_db, 80))

# Stressed decibel variation
def stressed_decibel_variation(cur_value, target=90, max_change=4):
    if cur_value < target:
        change = random.uniform(0, max_change)
    elif cur_value > target:
        change = -random.uniform(0, max_change)
    else:
        change = random.uniform(-max_change, max_change)

    next_db = cur_value + change
    return max(70, min(next_db, 100))
```

---

## Usage

To test the functions:
```python
# HR Stress Level Test
print("HR Stress Level Test:", hr_stress_level(60, 200))

# dB Stress Level Test
print("DB Stress Level Test:", db_stress_level(80))

# Overall Stress Level Test
print("Overall Stress Level Test:", overall_stress_level(60, 120, 80))
```

### Running the Application

1. Clone the repository.
2. Install the necessary dependencies.
3. Run the main application file using:
   ```bash
   python main.py
   ```

---

## Future Goals

Our goal is to transform CalmAlert into a fully functional wearable application for smartwatches, where it will continuously monitor and alert users of high-stress situations in real time.

---

## Authors

- **Sanaa Bhaidani** - Backend Developer
- **Jacob Mellick** - Full-Stack Developer
- **John Alvaro** - Full-Stack Developer
- **Grace Padberg** - Backend Developer
```
