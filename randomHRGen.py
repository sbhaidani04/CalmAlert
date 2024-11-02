import random

# Healthy heart rate (60 - 100 bpm)
normalHRMin = 60
normalHRMax = 100
normalHRAvg = (normalHRMin + normalHRMax) / 2  # Use float for precision

# Stress heart rate (150 - 220 bpm)
stressHRMin = 150
stressHRMax = 220
stressHRAvg = 200  # Use a value close to the middle of the stress range

def normalHRGenerator(pastVal):
    max_change = 2  # Adjust to control the rate of change

    if pastVal < normalHRAvg:
        change = random.uniform(0, max_change)
    elif pastVal > normalHRAvg:
        change = -random.uniform(0, max_change)
    else:
        change = random.uniform(-max_change, max_change)

    new_hr = pastVal + change
    new_hr = max(normalHRMin, min(new_hr, normalHRMax))
    return new_hr

def stressHRGenerator(pastVal):
    max_change = 2  # Adjust to control the rate of change

    # Ensure pastVal fluctuates around stressHRAvg with bounded noise
    change = random.uniform(-max_change, max_change)
    if pastVal < stressHRAvg:
        change += random.uniform(0, max_change / 2)  # Encourage a slight increase
    elif pastVal > stressHRAvg:
        change -= random.uniform(0, max_change / 2)  # Encourage a slight decrease

    new_hr = pastVal + change
    new_hr = max(stressHRMin, min(new_hr, stressHRMax))
    return new_hr
