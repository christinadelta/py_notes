# Run the Hierarchical Drift Diffusion Model (HDDM; Wiecki T.V, et al., 2013) on the discriminability data

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import hddm

# %matplotlib inline

# load the data
dt_data = hddm.load_csv('./hddm_dt_data.csv')

# dt data:
'''
subjects: 19 (0-18)
pairs: 666 (630 different, 36 same)
rt: reaction times (10 rts per different pair, 56 rts per same pair)
response: correct(1), incorrect(0)
condition: same objects pair(1), different objects pair(2)
'''

# add headers
headers = ["subNo", "pair", "rt", "response", "condition"]

dt_data.columns = headers

# in python indexing starts with zero, thus, subject one is actually zero. Change indexing
dt_data["subNo"] = dt_data["subNo"] - 1

# quick check
dt_data.head(20)

# sort the data
dt_sorted = dt_data.sort_values(by=['subNo'])

# flip error rts (0) to negative
data_negative = hddm.utils.flip_errors(dt_sorted)

# let's look at the rts distribution (on the left are the incorrect rts and on the right the correct ones)
fig = plt.figure()
ax = fig.add_subplot(111, xlabel='rt', ylabel='count', title='rt distribution')

for i , subj_data in data_negative.groupby('subNo'):
    subj_data.rt.hist(bins=20, histtype='step', ax=ax)

# plt.savefig('hddm_rts_distribution.pdf')

# create the model and run hddm
model = hddm.HDDM(dt_sorted, bias='True', depends_on={'a': 'pair', 'v': 'pair'},include=('sv', 'st', 'sz'))
# find a good starting point for the convergence
model.find_starting_values()

# draw samples
model.sample(2000, burn=50)

# look at the stats
stats = model.gen_stats()
stats[stats.index.isin(['a', 'a_std', 'v', 'v_std', 't', 't_std'])]

# given that I ran the model on bluebear, I'll save the stats df to work on it on my local machine
# stats.to_csv('./stats_allincluded.csv')
# I ran the model and saved the stats, now load it (if necessary) as a pandas dataframe.
#stats = pd.read_csv("stats_allincluded.csv")

# extract the averaged across subjects drifts (v) to use it for variance partitioning
drifts_averaged = stats.iloc[21:651, 1]

# save the averaged drifts - this will go to R for variance partitioning
drifts_averaged.to_csv('./averaged_drifts.csv')
