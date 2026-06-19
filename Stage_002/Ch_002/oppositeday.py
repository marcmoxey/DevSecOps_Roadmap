today_is_opposite_day = True

# set say_it_is_opposite_day base on today_is_opposite_day:
if today_is_opposite_day == True:
    say_it_is_opposite_day = True
else: 
    say_it_is_opposite_day = False 


# if it is opposite day, toggle say_it_is_opposite_day:
if today_is_opposite_day == True:
    say_it_is_opposite_day = not say_it_is_opposite_day

# Say What day it is:
if say_it_is_opposite_day == True:
    print('Today is Opposite Day.')
else: 
    print('Today is not Opposite Day.')