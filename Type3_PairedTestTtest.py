#운동 전후 체중 변화를 검정하시오.
#before: `[80, 82, 78, 79, 81]`
#after:  `[78, 80, 77, 78, 79]`
from scipy.stats import ttest_rel
import numpy as np

before = np.array([80,82,78,79,81])
after  = np.array([78,80,77,78,79])

stat, p = ttest_rel(before, after)

print(round(stat, 3))
print(round(p, 3))
