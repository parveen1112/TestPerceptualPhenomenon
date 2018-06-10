import math
import pandas

csv = pandas.read_csv('./stroopdata.csv')

cong = csv['Congruent']
incong = csv['Incongruent']

congMean = cong.mean()
incongMean = incong.mean()

congStd = cong.std()
incongStd = incong.std()

print("Congruent Mean", congMean)
print("Incongruent Mean", incongStd)
print("Congruent Deviation", congStd)
print("Incongruent Deviation", incongStd)


