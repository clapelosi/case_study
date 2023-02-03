from bs4 import BeautifulSoup, NavigableString, Tag 
import pandas as pd
import numpy as np

def clean_text(word):
    word_1 = word.strip()
    word_2 = word_1.strip('\n') 
    return word_2

def get_attribs_val(val):
  new_val = [value for key, value in val.items()]
  return new_val


def structure_xml(child):
   a = []
   temp = get_attribs_val(child.attrs)
   for val in temp:
      a.append(val)
   a.append(clean_text(child.text))
   if len(list(child.child) <= 1):
      return a
   else:
      return a + structure_xml(child.next_sibiling) + structure_xml(child.child)
   

def get_omogeneus_data(a, i):
    data = []
    for j in range(len(a)):
        if len(a[j]) == i:
            data.append(a[j])

    return data 
   
def trans(input_df,i,j):
    input_df.iloc[:,i] = input_df.iloc[:,i]*input_df.iloc[:,j]
    output_df = input_df
    
    return output_df