import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

#DEBUG MODES
debug = False
no_noise = False
show_true = False


random.seed( a=1738, )

# Ray
def true_value(a=0, b=0, c=0, x=0):
    return a*(x**2) + b*(x) + c

# Ray
def random_noise(r):
    if no_noise:
        return 0
    return (random.random() * r) - (r / 2) #random float between [-(range/2), (range/2)]

# Ray
# @param {s} start, noise x value range
# @param {e} end, noise x value range
# @return {list}
def get_data_and_noise(s, e):
    list = []
    for i in range(s, e+1):
        tru_val = true_value(a=2, b=7, c=5, x=i)
        yval = tru_val + random_noise(e**2)
        data = (i, yval, tru_val)
        list.append(data)
    return list

# Ray
# Returns the correct yhat formulat based on the degree of the polynomial
# @param {xs} a list of x values
# @param {ys} a list of y vales
# @return {list} a list containing the correct yhat formulas for given x values
def get_trendline(xs, ys, degree):
    list = []
    z = np.polyfit(xs, ys, degree)

    #iterate over the list of x values, assigning the correct yhat formula and appending to @return list[]
    for i, x in enumerate(xs):
        if degree == 1:
            yhat = x*z[0] + z[1]
        elif degree == 2:
            yhat = (x**2)*z[0] + x*z[1] + z[2]
        elif degree == 3:
            yhat = (x**3)*z[0] + (x**2)*z[1] + x*z[2] + z[3]
        elif degree == 4:
            yhat = (x**4)*z[0] + (x**3)*z[1] + (x**2)*z[2] + x*z[3] + z[4]
        else:
            raise Exception("INVALID DEGREE")
        list.append(yhat)
    return list

def get_residual(ys, yhats, x):
    return ys[x] - yhats[x]




start = 0
end = 50
list = get_data_and_noise(start, end)

xs = [x for (x,y,o) in list] #list of x values
ys = [y for (x,y,o) in list] #list of noisy data values
os = [o for (x,y,o) in list] #list of true function values
ls = get_trendline(xs, ys, 1)

plt.scatter(xs, ys)

if show_true:
    plt.plot(xs, os, color='r') #graph true line NOT the trendline

#show linear trendline
plt.plot(xs, ls, color='g')
diff = get_residual(ys, ls, (x-start))


plt.show()
if debug:
    print(list)
