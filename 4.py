# load library
import matplotlib.pyplot as plt
import pandas

csv = pandas.read_csv('./stroopdata.csv')


# this is a 'magic word' that allows for plots to be displayed
# inline with the notebook. If you want to know more, see:
# http://ipython.readthedocs.io/en/stable/interactive/magics.html:
#%matplotlib inline 

cong = csv['Congruent']
incong = csv['Incongruent']

plt.hist(cong)
plt.title('Congruent Hist')
plt.xlabel('Time (sec)')
plt.show()


plt.hist(incong)
plt.title('Incongruent hist')
plt.xlabel('Time (sec)')
plt.show()
