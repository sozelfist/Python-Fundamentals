import numpy as np


def linear_model(x, w, b):
    return w * x + b


def cost_function(x, y, w, b):
    predictions = linear_model(x, w, b)
    return ((predictions - y)**2).mean()


def adam(x, y, w, b, learning_rate, num_iterations, beta1=0.9, beta2=0.999, epsilon=1e-8):
    # initialize variables for momentum
    m_w = 0
    m_b = 0
    v_w = 0
    v_b = 0

    for i in range(num_iterations):
        # calculate gradients
        dw = (linear_model(x, w, b) - y).dot(x) / len(x)
        db = (linear_model(x, w, b) - y).mean()

        # update momentum
        m_w = beta1 * m_w + (1 - beta1) * dw
        m_b = beta1 * m_b + (1 - beta1) * db
        v_w = beta2 * v_w + (1 - beta2) * (dw**2)
        v_b = beta2 * v_b + (1 - beta2) * (db**2)

        # bias correction
        m_w_hat = m_w / (1 - beta1**(i + 1))
        m_b_hat = m_b / (1 - beta1**(i + 1))
        v_w_hat = v_w / (1 - beta2**(i + 1))
        v_b_hat = v_b / (1 - beta2**(i + 1))

        # update parameters
        w = w - learning_rate * m_w_hat / (np.sqrt(v_w_hat) + epsilon)
        b = b - learning_rate * m_b_hat / (np.sqrt(v_b_hat) + epsilon)

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

    # run Adam
    learning_rate = 0.01
    num_iterations = 2000
    final_w, final_b = adam(x, y, w, b, learning_rate, num_iterations)

    print(f'Final values: w = {final_w}, b = {final_b}')
