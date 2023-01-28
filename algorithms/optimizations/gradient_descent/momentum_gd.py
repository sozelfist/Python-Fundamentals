import numpy as np


def linear_model(x, w, b):
    return w * x + b


def cost_function(x, y, w, b):
    predictions = linear_model(x, w, b)
    return ((predictions - y)**2).mean()


def momentum_gradient_descent(x, y, w, b, learning_rate, num_iterations, momentum=0.9):
    v_dw = 0
    v_db = 0

    for i in range(num_iterations):
        # calculate gradients
        dw = (linear_model(x, w, b) - y).dot(x) / len(x)
        db = (linear_model(x, w, b) - y).mean()

        # update parameters with momentum
        v_dw = momentum * v_dw + (1 - momentum) * dw
        v_db = momentum * v_db + (1 - momentum) * db
        w = w - learning_rate * v_dw
        b = b - learning_rate * v_db

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
    num_iterations = 3000
    final_w, final_b = momentum_gradient_descent(x, y, w, b, learning_rate, num_iterations)

    print(f'Final values: w = {final_w}, b = {final_b}')
