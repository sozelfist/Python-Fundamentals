import numpy as np


def linear_model(x, w, b):
    return w * x + b


def cost_function(x, y, w, b):
    predictions = linear_model(x, w, b)
    return ((predictions - y)**2).mean()


def mini_batch_gradient_descent(x, y, w, b, learning_rate, num_iterations, batch_size):
    for i in range(num_iterations):
        # shuffle data
        indices = np.random.permutation(len(x))
        x = x[indices]
        y = y[indices]

        # split data into mini-batches
        for j in range(0, len(x), batch_size):
            x_batch = x[j:j + batch_size]
            y_batch = y[j:j + batch_size]

            # calculate gradients
            dw = ((linear_model(x_batch, w, b) - y_batch) * x_batch).mean()
            db = (linear_model(x_batch, w, b) - y_batch).mean()

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
    num_iterations = 1000
    batch_size = 2
    final_w, final_b = mini_batch_gradient_descent(x, y, w, b, learning_rate, num_iterations, batch_size)

    print(f'Final values: w = {final_w}, b = {final_b}')
