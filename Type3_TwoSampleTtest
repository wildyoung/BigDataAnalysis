#남자 그룹과 여자 그룹의 체중 평균이 동일한지 검정하시오.
#남자: `[72, 75, 70, 68, 74]`
#여자: `[60, 58, 62, 65, 59]`
from scipy.stats import ttest_ind
import numpy as np

g1 = np.array([72, 75, 70, 68, 74])
g2 = np.array([60, 58, 62, 65, 59])

stat, p = ttest_ind(g1, g2, equal_var=True)

print(round(stat, 3))
print(round(p, 3))
