# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 20:55:29 2022
@author: Rania Fleifel
"""
import pandas as pd;
import os
file_name='bank-full.csv'
df_bank=pd.read_csv(file_name,delimiter=';');

num_columns=len(df_bank.columns.tolist())
column_names=df_bank.columns.tolist()
print('\nInformation about',file_name)

print('\nNumber of columns= {} \n\nColumns names are {}'.format(num_columns,column_names));

print('\nNumber of entries= {}'.format(df_bank.size/num_columns));

print('\nSize of file= {} KB'.format(round(os.stat(file_name).st_size/1024),2));

print('\nNumber of duplicated entries= {}\n'.format(sum(df_bank.duplicated())));

print(df_bank.info());

#print(df_bank.describe());