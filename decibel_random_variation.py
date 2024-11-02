import random

def decibel_variation(cur_value):
    upper_bound = cur_value + 5
    lower_bound = cur_value - 5
    random_number = random.randint(lower_bound,upper_bound)
    return random_number
       

print(decibel_variation(30))


