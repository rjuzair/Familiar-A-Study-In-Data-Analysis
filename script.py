# Import libraries
import pandas as pd
import numpy as np
from scipy import stats

# Load datasets
lifespans = pd.read_csv('familiar_lifespan.csv')
iron = pd.read_csv('familiar_iron.csv')

#1 - 5
#print(lifespans.head())
vein_pack_lifespans = lifespans.lifespan[lifespans.pack == 'vein']
#print(vein_pack_lifespans)
vein_pack_lifespans_mean = np.mean(vein_pack_lifespans)
print(vein_pack_lifespans_mean)

tstat, pval = stats.ttest_1samp(vein_pack_lifespans, 73)
print(pval)
print('The life span of a vein pack subscriber is not 73')

#6 - 9
artery_pack_lifespans = lifespans.lifespan[lifespans.pack == 'artery']
#print(artery_pack_lifespans)
tstat, pval = stats.ttest_ind(artery_pack_lifespans, vein_pack_lifespans)
print(pval)
print('The average lifespan of both subscribers pack is equal')

#10
#print(iron.head())
Xtab = pd.crosstab(iron.pack, iron.iron)
print(Xtab)

chi2, pval, dof, expected = stats.chi2_contingency(Xtab)
print(pval)
print('there is association')
