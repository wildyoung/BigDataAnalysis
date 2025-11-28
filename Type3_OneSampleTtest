#한 집단의 평균 혈압(SBP)이 120과 다른지 검정하시오.
#샘플 데이터: `[128, 122, 130, 125, 119, 121, 127]`
#검정통계량과 p-value를 소수 셋째자리까지 출력하시오.

from scipy.stats import ttest_1samp
import numpy as np

x = np.array([128,122,130,125,119,121,127])
mu0 = 120

stat, p = ttest_1samp(x, mu0)

print(round(stat, 3))
print(round(p, 3))
