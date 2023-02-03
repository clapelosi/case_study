from bs4 import BeautifulSoup, NavigableString, Tag 
import pandas as pd
import numpy as np
import os 
os.chdir("./case_study")
from support_functions import clean_text, structure_xml, get_attribs_val, get_omogeneus_data

with open(r'C:\Users\39389\OneDrive\Desktop\my_repos\case_study\files\bilancio_test.xml', 'r') as f:
    file = f.read()
soup = BeautifulSoup(file, 'xml')
xbrl = soup.body.xbrl

obeject_des= []
attrib_values_raw = []
values_raw = []
for child in xbrl.children:
    if isinstance(child, NavigableString):
        continue
    if isinstance(child, Tag):
        obeject_des.append(child.name)
        attrib_values_raw.append(child.attrs)
        values_raw.append(child.text)      

attrib_values = []
for val in attrib_values_raw:
    attrib_values.append(get_attribs_val(val))

values = []
for val in values_raw:
    values.append(clean_text(val))

for i in range(len(attrib_values)):
    attrib_values[i].append(obeject_des[i])
    attrib_values[i].append(values[i])
  

a = attrib_values[5 :]

lengths = list(set(map(len, a)))
      


data_by_length = []
for i in range(len(lengths)):
    data_by_length.append(get_omogeneus_data(a, lengths[i]))
#    exec(f'data_{i} = data_i')               #not good method to not define the variables


header_3 = ['contextref', 'voice', 'description']
header_5 = ['contextref', 'decimals', 'unitref', 'voice', 'amount']
header_6 = ['contextref', 'decimals', 'nazione', 'unitref', 'voice', 'amount']

master_fin_stat_raw_df = pd.DataFrame(data_by_length[0], columns=header_3)
main_fin_stat_raw_df = pd.DataFrame(data_by_length[1], columns=header_5)
main_fin_stat_raw_2_df = pd.DataFrame(data_by_length[2], columns=header_6)

master_fin_stat_raw_df.to_csv('./raw_data/master_fin_stat_raw.csv', index=False, header=True)
main_fin_stat_raw_df.to_csv('./raw_data/main_fin_stat_raw.csv', index=False, header=True)
main_fin_stat_raw_2_df.to_csv('./raw_data/main_fin_stat_raw_2.csv', index=False, header=True)
  