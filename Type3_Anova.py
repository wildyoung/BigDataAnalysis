#세 그룹의 체지방률 평균이 같은지 검정하시오.
#Group1 = [22, 25, 23, 21]
#Group2 = [18, 20, 19, 17]
#Group3 = [30, 32, 31, 29]
from scipy.stats import f_oneway
import numpy as np

g1 = np.array([22,25,23,21])
g2 = np.array([18,20,19,17])
g3 = np.array([30,32,31,29])

stat, p = f_oneway(g1,g2,g3)

print(round(stat, 3))
print(round(p, 3))
