# -*- coding: utf-8 -*-
"""
Created on Sun May  6 11:39:05 2018

@author: Prometheus
"""

# Backward elimination with p-values only
import statsmodels.formula.api as sm
def backward_elimination(x, s1):
    num_vars = len(x[0])
    for i in range(0, num_vars):
        regressor_OLS = sm.OLS(y, x).fit()
        max_var = max(regressor_OLS.pvalues).astype(float)
        if max_var > s1:
            for j in range(0, num_vars -i):
                if (regressor_OLS.pvalues[j].astype(float) ==max_var):
                    x = np.delete(x, j, 1)
    regressor_OLS.summary()
    return x

SL = 0.05
X_opt =X[:, [0, 1, 2, 3, 4, 5]]
X_Modeled = backward_elimination(X_opt, SL)