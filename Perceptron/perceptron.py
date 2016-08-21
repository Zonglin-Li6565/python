import numpy as np
class Perceptron(object):                                           # The static class variables are declared in the class
    """Perceptron classifier"""
    def __init__(self, eta = 0.01, n_iter = 10):
        self.eta = eta                                              # The member variables are declared by self.var..
        self.n_iter = n_iter

    def fit(self, X, y):
        self.w = np.zeros(1 + X.shape[1])
        self.errors_ = []
        for _ in range(self.n_iter):
            errors = 0
            for xi, target in zip(X, y):
                update = self.eta * (target - self.predict(xi))
                self.w[1:] += update * xi
                self.w[0] += update
                errors += int(update != 0.0)
            self.errors_.append(errors)
        return self
    def net_input(self, X):
        return np.dot(X, self.w[1:]) + self.w[0];
    def predict(self, X):
        return np.where(self.net_input(X) >= 0.0, 1, -1)
