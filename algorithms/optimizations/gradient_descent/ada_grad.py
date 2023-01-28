import numpy as np


def linear_model(x, w, b):
    return w * x + b


def cost_function(x, y, w, b):
    predictions = linear_model(x, w, b)
    return ((predictions - y)**2).mean()


def adaptive_gradient_descent(x, y, w, b, learning_rate, num_iterations):
    # create a vector for the sum of the squared gradients
    sum_dw = 0
    sum_db = 0

    for i in range(num_iterations):
        # calculate gradients
        dw = (linear_model(x, w, b) - y).dot(x) / len(x)
        db = (linear_model(x, w, b) - y).mean()

        # update sum of squared gradients
        sum_dw += dw**2
        sum_db += db**2

        # update parameters with adaptive learning rate
        w = w - learning_rate * dw / (np.sqrt(sum_dw) + 1e-8)
        b = b - learning_rate * db / (np.sqrt(sum_db) + 1e-8)

        # calculate cost
        cost = cost_function(x, y, w, b)

        # print progress
        if (i + 1) % 1000 == 0:
            print(f'Iteration: {i+1}, cost = {cost}, w = {w}, b = {b}')
    return w, b


if __name__ == '__main__':

    # sample data
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([5, 7, 9, 11, 13])

    # initial values for parameters
    w = 1
    b = 1

    # run AdaGrad
    learning_rate = 0.01
    num_iterations = 20000
    final_w, final_b = adaptive_gradient_descent(x, y, w, b, learning_rate, num_iterations)

    print(f'Final values: w = {final_w}, b = {final_b}')
