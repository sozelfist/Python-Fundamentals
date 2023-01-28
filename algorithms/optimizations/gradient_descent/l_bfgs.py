from scipy.optimize import minimize
import numpy as np


def linear_model(x, w, b):
    return w * x + b


def cost_function(params, x, y):
    w, b = params
    predictions = linear_model(x, w, b)
    return ((predictions - y)**2).mean()


def grad_cost_function(params, x, y):
    w, b = params
    dw = (linear_model(x, w, b) - y).dot(x) / len(x)
    db = (linear_model(x, w, b) - y).mean()
    return np.array([dw, db])


if __name__ == '__main__':
    # sample data
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([5, 7, 9, 11, 13])

    # initial values for parameters
    params = [1, 1]

    # run L-BFGS
    res = minimize(cost_function, params, args=(x, y), method='L-BFGS-B', jac=grad_cost_function)

    final_w, final_b = res.x
    print(f'Final values: w = {final_w}, b = {final_b}')
