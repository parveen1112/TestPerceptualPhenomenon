# load library
import matplotlib.pyplot as plt
import pandas
from scipy.stats import t
import math

csv = pandas.read_csv('./stroopdata.csv')


cong = csv['Congruent']
incong = csv['Incongruent']


variance = (cong - incong).std()
sample_size = len(cong)
degrees_of_freedom = sample_size - 1

point_estimate = incong.mean() - cong.mean() # ui - uc

t_statistic = point_estimate / ( variance / math.sqrt(sample_size) )
t_critical = t.ppf(.95, degrees_of_freedom) # 95% confidence, 23 degrees of freedom

print("tCritical : ", t_critical, ". tStatistic: ", t_statistic, ". Point Estimate: ", point_estimate)
print("sample_size : ", sample_size, "variance", variance)
