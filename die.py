import random

# Roll 4d6 and Drop the lowest roll
def rollstats():
    # roll 4d6
    x = random.choices(range(1,6), k=4)
    # remove the lowest die and then get the total
    x.remove(min(x))
    y = sum(x)
    return(y)