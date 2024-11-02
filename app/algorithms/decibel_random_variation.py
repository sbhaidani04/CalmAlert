import random

def decibel_variation(cur_value):
    upper_bound = cur_value + 5
    lower_bound = cur_value - 5
    random_number = random.randint(lower_bound,upper_bound)
    return random_number
       

# print(decibel_variation(30))

def stressed_decibel_variation(cur_stressed_value, threshold = 130):
    if (cur_stressed_value < threshold):
        u_bound = cur_stressed_value + 4
        l_bound = cur_stressed_value - 1
    else:
        u_bound = cur_stressed_value + 1
        l_bound = cur_stressed_value - 1
    next_db = random.randint(l_bound,u_bound)
    return next_db

# # Testing function: 
# db = stressed_decibel_variation(30)
# for i in range(10):
#     db = stressed_decibel_variation(db)
#     print(db)
 
