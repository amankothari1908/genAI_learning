# importing numpy 
import numpy as np

# creating the statement 
# question :: Lee decides to walk 10000 steps every day to combat the effect that lockdown has had on his body’s agility, 
# mobility, flexibility and strength. Consider the following data from fitness tracker over a period of 10 days

day_number = [1,2,3,4,5,6,7,8,9,10]
steps_walked = [6012,7079,6886,7230,4598,5564,6971,7763,8023,9569]

# Represent the above data in a 10x2 array. In each row, 
# the first element should contain day number and second element should contain steps walked.
numpy_obj = np.array([day_number,steps_walked])
print(f"the numpy array created is : ${numpy_obj}")

# Lee notices that the tracker’s battery dies every day at 7 pm. Lee discovers that on an average, 
# he walks 2000 steps every day after 7 pm. Perform an appropriate operation on your array to add 2000 steps 
# to all the observations.
numpy_obj += 2000
print(f"the numpy array created is : ${numpy_obj}")

# Write a program that returns the steps walked if the steps walked are more than 9000.
indexes = np.where(numpy_obj[1] > 9000)
print(f"setps walked greater than 9000 are ${numpy_obj[1,indexes]}")

# Print an array containing steps walked in sorted order
print("setps in sorted order will be",np.sort(numpy_obj[1]))


