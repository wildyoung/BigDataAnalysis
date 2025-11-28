#  성공	실패
#A	30	20
#B	10	40
# 다음 교차표에 대해 독립성 검정을 수행하시오.
import numpy as np
from scipy.stats import chi2_contingency

data = np.array([
    [30,20],
    [10,40]
])

stat, p, dof, exp = chi2_contingency(data)

print(round(stat, 3))
print(round(p, 3))

