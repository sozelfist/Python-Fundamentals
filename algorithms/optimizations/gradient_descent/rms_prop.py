import numpy as np


def linear_model(x, w, b):
    return w * x + b


def cost_function(x, y, w, b):
    predictions = linear_model(x, w, b)
    return ((predictions - y)**2).mean()


def rmsprop(x, y, w, b, learning_rate, num_iterations, decay_rate=0.9, epsilon=1e-8):
    # initialize variables for moving average of squared gradients
    g_w = 0
    g_b = 0

    for i in range(num_iterations):
        # calculate gradients
        dw = (linear_model(x, w, b) - y).dot(x) / len(x)
        db = (linear_model(x, w, b) - y).mean()

        # update moving average of squared gradients
        g_w = decay_rate * g_w + (1 - decay_rate) * (dw**2)
        g_b = decay_rate * g_b + (1 - decay_rate) * (db**2)

        # update parameters
        w = w - learning_rate * dw / (np.sqrt(g_w) + epsilon)
        b = b - learning_rate * db / (np.sqrt(g_b) + epsilon)

        # calculate cost
        cost = cost_function(x, y, w, b)

        # print progress
        if (i + 1) % 10 == 0:
            print(f'Iteration: {i+1}, cost = {cost}, w = {w}, b = {b}')
    return w, b


if __name__ == '__main__':
    # sample data
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([5, 7, 9, 11, 13])

    # initial values for parameters
    w = 1
    b = 1

    # run RMSProp
    learning_rate = 0.01
    num_iterations = 300
    final_w, final_b = rmsprop(x, y, w, b, learning_rate, num_iterations)

    print(f'Final values: w = {final_w}, b = {final_b}')
