import numpy as np


def linear_model(x, w, b):
    return w * x + b


def cost_function(x, y, w, b):
    predictions = linear_model(x, w, b)
    return ((predictions - y)**2).mean()


def batch_gradient_descent(x, y, w, b, learning_rate, num_iterations):
    for i in range(num_iterations):
        # calculate gradients
        dw = ((linear_model(x, w, b) - y) * x).mean()
        db = (linear_model(x, w, b) - y).mean()

        # update parameters
        w = w - learning_rate * dw
        b = b - learning_rate * db

        # calculate cost
        cost = cost_function(x, y, w, b)

        # print progress
        if (i + 1) % 100 == 0:
            print(f'Iteration: {i+1}, cost = {cost}, w = {w}, b = {b}')
    return w, b


if __name__ == '__main__':

    # sample data
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([5, 7, 9, 11, 13])

    # initial values for parameters
    w = 1
    b = 1

    # run gradient descent
    learning_rate = 0.01
    num_iterations = 5000
    final_w, final_b = batch_gradient_descent(x, y, w, b, learning_rate, num_iterations)

    print(f'Final values: w = {final_w}, b = {final_b}')
