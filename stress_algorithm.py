import math

# HR stress level function (remains the same)
def hr_stress_level(user_avg_hr, user_cur_hr, k=0.02):
    hr_diff = user_cur_hr - user_avg_hr
    hr_stress = 50 * (1 - math.exp(-k * hr_diff))
    return hr_stress

# Updated dB stress level function to match the specified scale
def db_stress_level(decibel_value, threshold=70, k=0.07):
    if decibel_value > threshold:
        # Adjust scaling factor and k to fit the desired stress values
        scaled_stress = 50 * (1 - math.exp(-k * (decibel_value - threshold)))
        # Cap the maximum stress at 50 for dB levels ≥ 100
        return min(scaled_stress, 50)
    else:
        # Ensure stress is 0 if decibel value is below the threshold
        return 0

def overall_stress_level(user_average_hr, user_current_hr, db_value, threshold=70):
    hr_stress = hr_stress_level(user_average_hr, user_current_hr)
    db_stress = db_stress_level(db_value)
    stress_level = hr_stress + db_stress
    return stress_level

# # Test hr stress level:
# print("HR Stress Level Test:", hr_stress_level(60, 120))

# # Test db stress level:
# print("DB Stress Level Test:", db_stress_level(80))

# # Test overall stress level:
# print("Overall Stress Level Test:", overall_stress_level(60, 120, 80))

# # Test with various decibel levels to see how they align with the target scale
# print("\nDecibel Stress Level Tests:")
# for dB in [70, 75, 80, 85, 90, 95, 100, 110, 120]:
#     print(f"Decibels: {dB} -> Stress: {db_stress_level(dB):.2f}")
