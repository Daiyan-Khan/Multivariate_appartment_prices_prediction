# multivariate_linear_reg.py
import numpy as np
import pandas as pd

def compute_cost(x, y, w, b):
    m = x.shape[0]
    cost = 0.0
    for i in range(m):
        f_wb_i = np.dot(x, w) + b
        cost += (f_wb_i - y[i]) ** 2
    return cost / (2 * m)

def compute_gradient(x, y, w, b):
    m, n = x.shape
    dj_dw = np.zeros((n,))
    dj_db = 0
    for i in range(m):
        err = (np.dot(w, x[i]) + b) - y[i]
        for j in range(n):
            dj_dw[j] += (err * x[i, j])
        dj_db += err
    return dj_dw / m, dj_db / m

def gradient_descent(x, y, w_in, b_in, a, num_iters):
    J_hist = []
    w = np.copy(w_in)
    b = b_in
    for i in range(num_iters):
        dj_dw, dj_db = compute_gradient(x, y, w, b)
        w -= a * dj_dw
        b -= a * dj_db
    return w, b

def z_score_normalization(x):
    mu = np.mean(x, axis=0)
    sigma = np.std(x, axis=0)
    return (x - mu) / sigma

def predict(x, w, b):
    m, n = x.shape
    f = np.zeros((m,))
    x_temp = np.copy(x)
    for i in range(m):
        x_temp[i, 4] = x[i, 4] ** 3
        x_temp[i, 18] = x[i, 18] ** 3
        x_temp[i, 0] = x[i, 0] ** 0.15
        x_temp[i, 1] = x[i, 1] ** 0.5
        f[i] = np.dot(x_temp[i], w) + b
    return f
