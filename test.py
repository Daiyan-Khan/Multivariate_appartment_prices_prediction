import pytest
import numpy as np
from multivariate_linear_reg import compute_cost, compute_gradient, gradient_descent, z_score_normalization, predict

# Sample data for testing
@pytest.fixture
def sample_data():
    x = np.array([[1, 2], [2, 3], [3, 4]])
    y = np.array([3, 5, 7])
    return x, y

def test_compute_cost(sample_data):
    x, y = sample_data
    w = np.array([1, 1])
    b = 1
    cost = compute_cost(x, y, w, b)
    expected_cost = 0.5  # Manually calculated expected cost
    assert np.isclose(cost, expected_cost, rtol=1e-5)

def test_compute_gradient(sample_data):
    x, y = sample_data
    w = np.array([1, 1])
    b = 1
    dj_dw, dj_db = compute_gradient(x, y, w, b)
    expected_dj_dw = np.array([0.66666667, 0.66666667])  # Manually calculated expected gradients
    expected_dj_db = 0.66666667
    assert np.allclose(dj_dw, expected_dj_dw, rtol=1e-5)
    assert np.isclose(dj_db, expected_dj_db, rtol=1e-5)

def test_gradient_descent(sample_data):
    x, y = sample_data
    w_init = np.zeros(2)
    b_init = 0
    a = 0.01
    num_iters = 1000
    w, b = gradient_descent(x, y, w_init, b_init, a, num_iters)
    
    # Check if weights are updated (not equal to initial weights)
    assert not np.array_equal(w, w_init)
    assert not np.isclose(b, b_init, rtol=1e-5)

def test_z_score_normalization():
    x = np.array([[1, 2], [3, 4], [5, 6]])
    x_norm = z_score_normalization(x)
    expected_norm = np.array([[-1.41421356, -1.41421356],
                               [0.0, 0.0],
                               [1.41421356, 1.41421356]])
    assert np.allclose(x_norm, expected_norm, rtol=1e-5)

def test_predict(sample_data):
    x, y = sample_data
    w = np.array([1, 1])
    b = 1
    predictions = predict(x, w, b)
    expected_predictions = np.array([4, 5, 6])  # Manually calculated expected predictions
    assert np.allclose(predictions, expected_predictions, rtol=1e-5)
