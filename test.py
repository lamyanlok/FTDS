import numpy as np
import statistics
from scipy import stats

dataset= [5,6,7,5,6,5,7,4,5,5,5,5,7,5,6,6,7,6,6,7,7,7,6,5,6]

#mean value
mean= np.mean(dataset)

#median value
median = np.median(dataset)

#mode value
mode= stats.mode(dataset)

#standard Deviation
Std = statistics.stdev(dataset)

#Variance
Var = statistics.variance(dataset)

print("Mean: ", mean)
print("Median: ", median)
print("Mode: ", mode)
print("Std", Std)
print("Var", Var)
