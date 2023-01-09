import matplotlib.pyplot as plt

# Euler method
def euler(func, x0, y0, xn, n):
    x_array = []
    y_array = []
    # Calculating step size
    h = (xn-x0)/n

    for i in range(n):
        slope = func(y0, x0) #functions (M, t) or (T, t)
        yn = y0 + h * slope
        x_array.append(x0)
        y_array.append(y0)

        y0 = yn
        x0 = x0+h

    plt.plot(x_array, y_array, label='eulers')
    plt.legend()
    plt.show()

