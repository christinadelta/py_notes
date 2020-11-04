# Simple .py script for analysing the scores of the big-5 personality test. The scores are stored in a json file. 
# Author: ChristinaDelta
# October 2019

import os
import sys
import json


rootdir = f'/Users/christinadelta/Desktop'
big5dir = os.path.join(rootdir, 'meadows_big5_examples')

# import json file
print('reading json file')

jsonfile = os.path.join(big5dir, 'Meadows_PersonalityTest_RavensMatrices_v_v2_saving-quagga_2_tree.json')

# open the json_file. This is a dict that contains the items and responses
with open(jsonfile, 'r') as read_file:
    data = json.load(read_file)

# remove not needed keys and values
entries_to_remove = ('stimuli', 'token', 'status', 'qualification', 'task')

values_to_remove = ('Very Inaccurate', 'Moderately Inaccurate', 'Neither Accurate Nor Inaccurate', 'Moderately Accurate', 'Very Accurate')

# delete key-value pairs we don't need
for key in entries_to_remove:
    if key in data:
        del data[key]

# save keys in a list
allkeys_list = list(data.keys())
print(len(allkeys_list))
print(allkeys_list)

# split values to number and text and save them in a list
allvalues_list = [value.split('-') for value in data.values()]
print(allvalues_list)

new_valueslist = []

for i in allvalues_list:
    for item in i:
        new_valueslist.append(item)

# delete text part of values
for j in values_to_remove:
    while j in new_valueslist:
        new_valueslist.remove(j)

print(len(new_valueslist))

# convert values to int from str
new_valueslist = list(map(int, new_valueslist))

# zip the two lists back into a dict
big5_dict = dict(zip(allkeys_list, new_valueslist))

# the big5dir holds key-value pairs from 5 different factors. Define the keys of each factor separately
# keys of extroversion
factor1_keys = ["1", "6", "11", "16", "21", "26", "31", "36", "41", "46"]

# keys of agreeableness
factor2_keys = ["2", "7", "12", "17", "22", "27", "32", "37", "42", "47"]

# keys for conscientiousness
factor3_keys = ["3", "8", "13", "18", "23", "28", "33", "38", "43", "48"]

# keys for neuroticism
factor4_keys = ["4", "9", "14", "19", "24", "29", "34", "39", "44", "49"]

# keys for openness
factor5_keys = ["5", "10", "15", "20", "25", "30", "35", "40", "45", "50"]


# re-arrange the the big5 dict, split the keys/values in their corresponding factors (e.g extroversion factor gets the keys 1,6,11...)
factor1 = dict((k, big5_dict[k]) for k in factor1_keys if k in big5_dict)
factor2 = dict((k, big5_dict[k]) for k in factor2_keys if k in big5_dict)
factor3 = dict((k, big5_dict[k]) for k in factor3_keys if k in big5_dict)
factor4 = dict((k, big5_dict[k]) for k in factor4_keys if k in big5_dict)
factor5 = dict((k, big5_dict[k]) for k in factor5_keys if k in big5_dict)

# now calculate the scores for each factor
e = [20 + factor1['1'] - factor1['6'] + factor1['11'] - factor1['16'] + factor1['21'] - factor1['26'] + factor1['31'] - factor1['36'] + factor1['41'] - factor1['46']]

a = [14 - factor2['2'] + factor2['7'] - factor2['12'] + factor2['17'] - factor2['22'] + factor2['27'] - factor2['32'] + factor2['37'] + factor2['42'] + factor2['47']]

c = [14 + factor3['3'] - factor3['8'] + factor3['13'] - factor3['18'] + factor3['23'] - factor3['28'] + factor3['33'] - factor3['38'] + factor3['43'] + factor3['48']]

n = [38 - factor4['4'] + factor4['9'] - factor4['14'] + factor4['19'] - factor4['24'] - factor4['29'] - factor4['34'] - factor4['39'] - factor4['44'] - factor4['49']]

o = [8 + factor5['5'] - factor5['10'] + factor5['15'] - factor5['20'] + factor5['25'] - factor5['30'] + factor5['35'] + factor5['40'] + factor5['45'] + factor5['50']]
