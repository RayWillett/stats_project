import random
import numpy as np
import matplotlib.pyplot as plt

#CONFIG
debug = False
no_noise = False

show_true = True
show_fig = True
save_images = True


def true_value(a=0, b=0, c=0, x=0):
    return a*(x**2) + b*(x) + c

def random_noise(r):
    if no_noise:
        return 0
    return (random.random() * r) - (r / 2)

def get_noisy_data(s, e, data, r=100):
    list1 = []
    for i in range(s, e+1):
        tru_val = data[i]
        yval = tru_val + random_noise(r)
        noisy = (i, yval, tru_val) #x, y, o
        list1.append(noisy)
    return list1

def get_data(s, e):
    list1 = []
    for i in range(s, e+1):
        true_val = true_value(a=1, b=-40, c=2100, x=i)
        list1.append(true_val)
    return list1

def get_residual(ys, yhats, x):
    return ys[x] - yhats[x]


def get_trendline(xs, ys, degree):
    list = []
    coeff = [0, 0, 0, 0, 0] #list of coefficients, where index is the power
    z = np.polyfit(xs, ys, degree)

    #iterate over the list of x values, assigning the correct yhat formula and appending to @return list[]
    for i, x in enumerate(xs):
        if degree == 0:
            yhat = z[0]
            coeff[0] = z[0]
        elif degree == 1:
            yhat = x*z[0] + z[1]
            coeff[1] = z[0]
            coeff[0] = z[1]
        elif degree == 2:
            yhat = (x**2)*z[0] + x*z[1] + z[2]
            coeff[2] = z[0]
            coeff[1] = z[1]
            coeff[0] = z[2]
        elif degree == 3:
            yhat = (x**3)*z[0] + (x**2)*z[1] + x*z[2] + z[3]
            coeff[3] = z[0]
            coeff[2] = z[1]
            coeff[1] = z[2]
            coeff[0] = z[3]
        elif degree == 4:
            yhat = (x**4)*z[0] + (x**3)*z[1] + (x**2)*z[2] + x*z[3] + z[4]
            coeff[4] = z[0]
            coeff[3] = z[1]
            coeff[2] = z[2]
            coeff[1] = z[3]
            coeff[0] = z[4]
        else:
            raise Exception("INVALID DEGREE")
        list.append(yhat)
    return (list, coeff)


def extrapolate_trendline(xs, z, d):
    values = []
    if d == 4:
        for x in xs:
            value = z[4] * x**4 + z[3] * x**3 + z[2] * x**2 + z[1] * x + z[0]
            values.append(value)
    elif d == 3:
        for x in xs:
            value = z[3] * x ** 3 + z[2] * x ** 2 + z[1] * x + z[0]
            values.append(value)
    elif d == 2:
        for x in xs:
            value = z[2] * x**2 + z[1] * x + z[0]
            values.append(value)
    elif d == 1:
        for x in xs:
            value = z[1] * x + z[0]
            values.append(value)
    elif d == 0:
        for x in xs:
            value = z[0]
            values.append(value)
    return values

def iterate(d, n=10):
    trend_start = 0
    trend_end = 50
    graph_end = 75

    data = get_data(trend_start, graph_end)

    #save figure file directory and extension


    base = "../images/" + "degree" + str(d) + "/tradeoff/image_"
    ext = ".png"

    fig, (scatter) = plt.subplots(nrows=1, ncols=1)
    for i in range(n):
        fig.suptitle("Bias vs Variance")

        fig.tight_layout()
        scatter.clear()
        list1 = get_noisy_data(trend_start, graph_end, data, r=400)

        xs, ys, os = [list(elem) for elem in zip(*list1)]
        (_, z) = get_trendline(xs[trend_start:trend_end], ys[trend_start:trend_end], d)
        #(ls, z) = get_trendline(xs, ys, d)

        ls = extrapolate_trendline(xs, z, d);
        print(ys)

        #show linear trendline
        if show_fig:
            scatter.scatter(xs, ys)
            scatter.plot(xs, ls, color='r')

            if show_true:
                scatter.plot(xs, os, color='b') #graph true line NOT the trendline

            fig.tight_layout()
            fig.canvas.draw() #
            fig.show()
            if save_images:
                fig.savefig(base + str(i).rjust(2, '0') + ext)
iterate(0) #generate 10 of them and pick the best