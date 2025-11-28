import statsmodels.api as sm
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'x1':[1,2,3,4],
    'x2':[3,2,1,1],
    'y':[1,1,0,0]
})

X = df[['x1','x2']]
X = sm.add_constant(X)
y = df['y']

# GLM 방식 (Binomial + 기본 링크 logit)
glm_model = sm.GLM(y, X, family=sm.families.Binomial()).fit()

print(glm_model.params)          # 회귀계수
print(np.exp(glm_model.params))  # odds ratio (exp(beta))
print(glm_model.pvalues)         # p-value
