import random
import time

# define parameters for the range
regular_lower_bound = 28
regular_upper_bound = 60
regular_generated = []
regular_label = "regular"

stressed_lower_bound = 60
stressed_upper_bound = 100
stressed_generated = []
stressed_label = "stressed"


count = 5

def rand_generation(count, lower_bound, upper_bound, array, label):
    for i in range(count):
        random_number = random.randint(lower_bound, upper_bound)
        array.append(random_number)
        print("Random", label, "number generated: ", random_number)
        time.sleep(3)
    return array

regular_result = rand_generation(count, regular_lower_bound, regular_upper_bound, regular_generated, regular_label)
print(regular_result)

stressed_result = rand_generation(count, stressed_lower_bound, stressed_upper_bound, stressed_generated, stressed_label)
print(stressed_result)


