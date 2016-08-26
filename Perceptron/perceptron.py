import numpy as np
class ADAlineGD(object):                                              # The static class variables are declared in the class
    """ADAptive classifier"""
    def __init__(self, eta = 0.01, n_iter = 10):
        self.eta = eta                                                # The member variables are declared by self.var..
        self.n_iter = n_iter
        #self.w_ = []
        #self.cost_ = []

    def fit(self, X, y):
        self.w_ = np.zeros(1 + X.shape[1])
        self.cost_ = []
        for i in range(self.n_iter):
            #errors = y - self.net_input(X)
            #self.w_[1:] -= self.eta * X.T.dot(errors)                # eta * \sig(y_i- z_i) * x_i
            #self.w_[0]  -= self.eta * errors.sum()                   # x_0 = 1
            #self.cost_.append((errors ** 2).sum() * 0.5)             # append errors
            output = self.net_input(X)
            errors = (y - output)
            self.w_[1:] += self.eta * X.T.dot(errors)
            self.w_[0]  += self.eta * errors.sum()
            cost = ((errors ** 2).sum() / 2.0)
            self.cost_.append(cost)
        return self
    def net_input(self, X):
        return np.dot(X, self.w_[1:]) + self.w_[0];
    def predict(self, X):
        return np.where(self.net_input(X) >= 0.0, 1, -1)

def main ():
    import numpy as np
    import pandas as pd
    print("starts importing data...")
    df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', header=None)
    print("finished importing data")
    y = np.where (df.iloc[:, 4].values == 'Iris-setosa', -1, 1)
    X = df.iloc[:, [0, 2]].values
    print ("shape of y: ", y.shape, " shape of X: ", X.shape)
    X_std = np.copy(X)
    X_std[:, 0] = (X[:, 0] - X[:, 0].mean()) / X[:, 0].std()
    X_std[:, 1] = (X[:, 1] - X[:, 1].mean()) / X[:, 1].std()
    ada = ADAlineGD(eta = 0.01, n_iter = 10).fit(X_std, y)
    print("training finished")
    from plot_decision_region import plot_decision_regions
    import matplotlib.pyplot as plt
    plot_decision_regions(X_std, y, classifier = ada)
    plt.title ('adaline - gradient descent')
    plt.show()
    plt.plot(range(1, len(ada.cost_) + 1), ada.cost_, marker = 'o')
    plt.xlabel('Epoches')
    plt.ylabel('Sum-squared-error')
    plt.show()
main()
