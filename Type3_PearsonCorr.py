#키와 몸무게의 상관계수를 구하고 유의성을 검정하시오.
#height = [160, 165, 170, 175, 180]
#weight = [55, 60, 65, 72, 78]
from scipy.stats import pearsonr, spearmanr
import numpy as np

h = np.array([160,165,170,175,180])
w = np.array([55,60,65,72,78])

# Pearson 상관계수 + p-value
r_p, p_p = pearsonr(h, w)

# Spearman 상관계수 + p-value
r_s, p_s = spearmanr(h, w)

print("Pearson:", round(r_p, 3), round(p_p, 3))
print("Spearman:", round(r_s, 3), round(p_s, 3))
