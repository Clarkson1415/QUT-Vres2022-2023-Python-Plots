import matplotlib.pyplot as plt

# Euler method
def euler(func, x0,y0,xn,n):
    x_array = []
    y_array = []
    # Calculating step size
    h = (xn-x0)/n

    print('\n-----------SOLUTION-----------')
    print('------------------------------')
    print('x0\ty0\tslope\tyn')
    print('------------------------------')
    for i in range(n):
        slope = func(x0, y0)
        yn = y0 + h * slope
        print('%.4f\t%.4f\t%0.4f\t%.4f'% (x0,y0,slope,yn) )
        print('------------------------------')
        x_array.append(x0)
        y_array.append(y0)

        y0 = yn
        x0 = x0+h

    print('\nAt x=%.4f, y=%.4f' %(xn,yn))
    plt.plot(x_array, y_array, label='eulers')
    plt.legend()
    plt.show()

# Euler method call
#euler(x0,y0,xn,step)

