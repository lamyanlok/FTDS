import math
def birthday_probability(n):

    # Formula taken from: https://en.wikipedia.org/wiki/Birthday_problem
    return 1 - math.e ** (-n**2 / (2 *365))

n = int(input("Pls input the number of people in room"))
probability = birthday_probability(n)
print('Probability is {}, or about 1 in {:,d}'.format(probability, int(round(1 / probability))))