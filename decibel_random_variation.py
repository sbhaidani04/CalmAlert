import random

# Normal decibel variation aiming for an average of 60 dB
def normal_decibel_variation(cur_value, target=60, max_change=5):
    # Calculate the direction to move towards the target
    if cur_value < target:
        change = random.uniform(0, max_change)  # Positive change
    elif cur_value > target:
        change = -random.uniform(0, max_change)  # Negative change
    else:
        change = random.uniform(-max_change, max_change)  # Small fluctuation at the target

    # Apply the change and constrain within reasonable bounds (e.g., 40 to 80)
    next_db = cur_value + change
    return next_db

# Stressed decibel variation aiming for an average of 90 dB
def stressed_decibel_variation(cur_value, target=90, max_change=4):
    # Calculate the direction to move towards the target
    if cur_value < target:
        change = random.uniform(0, max_change)  # Positive change
    elif cur_value > target:
        change = -random.uniform(0, max_change)  # Negative change
    else:
        change = random.uniform(-max_change, max_change)  # Small fluctuation at the target

    # Apply the change and constrain within reasonable bounds (e.g., 70 to 100)
    next_db = cur_value + change
    return next_db

# # Testing the functions
# print("Normal Decibel Variation Test:")
# db = 50  # Starting value
# for _ in range(20):
#     db = normal_decibel_variation(db)
#     print(f"Normal dB: {db:.2f}")

# print("\nStressed Decibel Variation Test:")
# db_stressed = 85  # Starting value
# for _ in range(20):
#     db_stressed = stressed_decibel_variation(db_stressed)
#     print(f"Stressed dB: {db_stressed:.2f}")
