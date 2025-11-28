import statsmodels.api as sm
import pandas as pd

df = pd.DataFrame({
    'age':[30,40,50,60],
    'bmi':[22,25,27,30],
    'y':[120,130,150,170]
})

X = df[['age','bmi']]
X = sm.add_constant(X)
y = df['y']

model = sm.OLS(y, X).fit()

print(round(model.rsquared, 3))     # R^2
print(model.params)                # 회귀계수
print(model.pvalues)               # p-value

