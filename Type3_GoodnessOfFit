#관측도수는 [50, 30, 20],
#기대비율은 4:3:3
#적합도 검정을 수행하시오.
from scipy.stats import chisquare

obs = [50, 30, 20]
exp = [40, 30, 30]

stat, p = chisquare(obs, exp)

print(round(stat, 3))
print(round(p, 3))
