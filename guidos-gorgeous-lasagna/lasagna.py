# TODO: define the 'EXPECTED_BAKE_TIME' constant
EXPECTED_BAKE_TIME=40   
# TODO: consider defining the 'PREPARATION_TIME' constant
#       equal to the time it takes to prepare a single layer
PREPARATION_TIME=2 

# TODO: define the 'bake_time_remaining()' function
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.
        Function that takes the actual minutes the lasagna has been in the oven as
        an argument and returns how many minutes the lasagna still needs to bake
        based on the `EXPECTED_BAKE_TIME`.
    """
    minutes_left=EXPECTED_BAKE_TIME-elapsed_bake_time
    return minutes_left

# TODO: define the 'preparation_time_in_minutes()' function
#       and consider using 'PREPARATION_TIME' here
def preparation_time_in_minutes(number_of_layers):
    """ Return preparation time. 
        This function takes the number of layers you want to add to the 
        lasagna as an argument and returns how many minutes you would spend making them
    
    """
    preparingtime=number_of_layers*PREPARATION_TIME
    return preparingtime
    
# TODO: define the 'elapsed_time_in_minutes()' function
def elapsed_time_in_minutes(number_of_layers,elapsed_bake_time):
    """ Return elapsed cooking time.
        This function takes two numbers representing the number of layers & the time already spent 
        baking and calculates the total elapsed minutes spent cooking the lasagna.
    """
    elapsed_time=elapsed_bake_time+(number_of_layers*PREPARATION_TIME)
    return elapsed_time

#PRINT EXAMPLES: 

print (bake_time_remaining(20))
print (preparation_time_in_minutes(3))
print (elapsed_time_in_minutes(3,20))