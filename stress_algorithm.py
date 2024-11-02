import math
# determining the stress algorithm 
# want values either due to heart rate or decibel level
# or a combination of both - cumulative stress level
# should utilize the baseline of a user's average resting heart rate

# stress levels are from 0 to 100
def hr_stress_level(user_avg_hr, user_cur_hr, k = 0.02):
    hr_diff = user_cur_hr - user_avg_hr
    decibel_stress = 50 * (1 - math.exp(-k * (hr_diff)))
    return decibel_stress

def db_stress_level(decibel_value, threshold = 70, k = 0.1):
    if (decibel_value > threshold):
        # determine and add the stress level contribution by decibel level
        decibel_stress = 50 * (1 - math.exp(-k * (decibel_value - threshold)))
    return decibel_stress

def determine_stress_level(user_avg_hr, user_cur_hr, decibel_value, threshold = 70, k = 0.1):
    stress_level = 0
    hr_diff = user_cur_hr - user_avg_hr
    if (hr_diff > 20):
        # add the stress level contribution by hr
        stress_level += hr_diff

    if (decibel_value > threshold):
        # determine and add the stress level contribution by decibel level
        decibel_stress = 50 * (1 - math.exp(-k * (decibel_value - threshold)))
        stress_level += decibel_stress
    
    return stress_level

# Test hr stress level:
print(hr_stress_level(60, 120))

# Test db stress level:
print(db_stress_level(80))

# Test with various decibel levels
for dB in [70, 75, 80, 85, 90, 95, 100, 120]:
    print(f"Decibels: {dB} -> Stress: {determine_stress_level(10, 10, dB):.2f}")