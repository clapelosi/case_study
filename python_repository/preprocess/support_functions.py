from bs4 import BeautifulSoup, NavigableString, Tag 
import pandas as pd
import numpy as np

# SUPPORT FUNCTION TO CLEAN THE TEXT TAGS FORM '\n' AND VLANKS ' '
def clean_text(word):
    word_1 = word.strip()
    word_2 = word_1.strip('\n') 
    return word_2


# SUPPORT FUNCTION TO EXTRAPOLATE THE ATTRIBUTES VALUES OF A TAG AS A LIST
def get_attribs_val(val):
  new_val = [value for key, value in val.items()]
  return new_val

# SUPPPORT RECORSIVE FUNTION FROM A LIST OF TAGS TO EXTRAPOLATE A TABULAR FOR OF VALUES
# !! NOT FINISHED - TO WORK ON THE RECURSION AND TO EXTRAPOLATE HEADERS !!
def structure_xml(child):
   a = []
   temp = get_attribs_val(child.attrs)
   for val in temp:
      a.append(val)
   a.append(clean_text(child.text))
   if len(list(child.child) <= 1):
      return a
   else:
    # older_child = child.child 
    # child.child.next_sibiling = young_child
    # return a + structure_xml(older_child) + structure_xml(young_child) 
      return a + structure_xml(child.next_sibiling) + structure_xml(child.child)
   
#SUPPORT FUNCTION USED IN AN EASY APPROCH ON THE USED PROSES TO SPLIT THE ETEREGENOUS DATA ON "THE COLUMNS NUMBER"
def get_omogeneus_data(a, i):
    data = []
    for j in range(len(a)):
        if len(a[j]) == i:
            data.append(a[j])

    return data 

# SUPPORT FUNCTION  TO MULTIPLICATE COLUMNS VALUES OF A DATAFRAME 
def trans(input_df,i,j):
    input_df.iloc[:,i] = input_df.iloc[:,i]*input_df.iloc[:,j]
    output_df = input_df
    
    return output_df