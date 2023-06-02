# power_dependence_list.py: list the possible powers and randomize the list for power dependence measurements
# May 31st, 2023 by Samihat Rahman
import datetime
import pandas as pd
import random as rand

# input here
max_power = 71.2
min_power = 0.6
factor = 1.3 
save = False

# recursive function that spits out the list
def powers(max_power, min_power, factor):
    # base case
    if max_power <= min_power:
        return [max_power]
    return [max_power] + powers(max_power/factor, min_power, factor)
    
# calling the function
powers_list = powers(max_power, min_power, factor)

# round to three decimal points
powers_list = [round(i, 3) for i in powers_list]

# automatically pull the current date for naming the file
date = datetime.datetime.now()
date_string = date.strftime("%Y-%m-%d").replace('/', '-')

# create copies of the list for trials
powers_list_1 = powers_list.copy()
powers_list_2 = powers_list.copy()
powers_list_3 = powers_list.copy()

# shuffle each list
rand.shuffle(powers_list_1)
rand.shuffle(powers_list_2)
rand.shuffle(powers_list_3)

# dataframe which stores the shuffled powers
dataframe = pd.DataFrame({'Trial 1': powers_list_1, 'Trial 2': powers_list_2, 'Trial 3': powers_list_3})

# save the dataframe
if save:
    dataframe.to_csv(f'{date_string} List of Powers.csv', index=False)
