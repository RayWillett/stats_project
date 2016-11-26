import random
import matplotlib.pyplot as plt

#DEBUG MODES
debug = True
no_noise = False
show_true = True


random.seed(a=1738, version=2)

def true_value(a=0, b=0, c=0, x=0):
    return a*(x**2) + b*(x) + c

def random_noise(r):
    if no_noise:
        return 0
    return (random.random() * r) - (r / 2) #random float between [-(range/2), (range/2)]

def get_data_and_noise(s, e): #start, end, noise's range
    list = []
    for i in range(s, e+1):
        tru_val = true_value(a=2, b=7, c=5, x=i)
        yval = tru_val + random_noise(e**2)#TODO: is this the best range for noise?
        data = (i, yval, tru_val)
        list.append(data)
    return list

list = get_data_and_noise(0, 50)

xs = [x for (x,y,o) in list] #list of x values
ys = [y for (x,y,o) in list] #list of noisy data values
os = [o for (x,y,o) in list] #list of true function values

plt.scatter(xs, ys)

if show_true:
    plt.plot(xs, os, color='r') #graph true line NOT the trendline




plt.show()
if debug:
    print(list)
