import pandas as pd
import numpy as np
from support_functions import trans
import os 
os.chdir("./case_study")

transaction_df = pd.read_csv(r"C:\Users\39389\OneDrive\Desktop\my_repos\case_study\data\Transazioni_Azienda_ABC.csv")
transaction_df.rename(columns = {'data ':'date', 'categoria':'category', 'amount':'amt'}, inplace = True)
transaction_df['date'] = pd.to_datetime(transaction_df['date'], format="%d/%m/%Y")
transaction_df.replace(to_replace=r'€ ', value='', regex=True, inplace=True)
transaction_df['amt'].replace(to_replace=r'\.', value= '', regex=True, inplace=True)
transaction_df['amt'].replace(to_replace=r',', value= '.', regex=True, inplace=True)
transaction_df['amt'] = transaction_df['amt'].astype('float64')

trans_transformed1_df = pd.get_dummies(transaction_df, columns=['category'])

trans_transformed1_df.to_csv('./cleaned_data/trans_transformed1.csv', index=False, header=True)


for i in range(2,trans_transformed1_df.shape[1]):
    trans_transformed2_df = trans(trans_transformed1_df,i,1)



trans_transformed2_df.rename(columns = {'category_EROGAZIONE FINANZIAMENTO':'loan_disbursement', 
                                        'category_INCASSO FATTURA':'bill_incomes', 
                                        'category_PAGAMENTO FATTURA':'bill_outcomes',
                                        'category_PAGAMENTO FORNITORI':'supplier_outcomes',
                                        'category_RIMBORSO FINANZIAMENTO':'loan_repayments',
                                        'category_STIPENDI':'salaries',
                                        'category_UTENZE':'utilities', 'amount':'amt'}, inplace = True)

trans_transformed2_df.drop(columns=['amt'], inplace=True)

trans_transformed2_df.to_csv('./cleaned_data/trans_transformed2.csv', index=False, header=True)



