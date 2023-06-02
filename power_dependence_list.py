# power_dependence_list.py: list the possible powers spaced by a factor and randomize the list for power dependence measurements
# June 2nd, 2023 by Samihat Rahman
import datetime
import numpy as np
import pandas as pd
import random as rand

# input here
max_power = 71.2
min_power = 0.6
factor = 1.3 

# number of trials
trials = 3

# if you want to save as csv
save = True

# recursive function that spits out the list
def powers(max_power, min_power, factor):
    # base case
    if max_power <= min_power:
        return [max_power]
    # recursive addition
    return [max_power] + powers(max_power/factor, min_power, factor)
    
# calling the function
powers_list = powers(max_power, min_power, factor)

# round to three decimal points
powers_list = [round(i, 3) for i in powers_list]

# create a data frame to save the data
dataframe = pd.DataFrame()
trials_list = np.arange(1, trials+1)

# shuffle and save to each trial
for trial in trials_list:
    power_list_temp = powers_list.copy()
    rand.shuffle(power_list_temp)
    dataframe[f'Trial {trial}'] = power_list_temp

# for a column with the powers arranged least to greatest
reversed_powers = powers_list.copy()
reversed_powers.reverse()

dataframe['Powers'] = reversed_powers

# final data frame
print(dataframe)

# save by date of creation
date = datetime.datetime.now()
date_string = date.strftime("%Y-%m-%d").replace('/', '-')

if save:
    dataframe.to_csv(f'{date_string} List of Powers.csv', index=False)
