import pandas as pd
import csv
import os

current_dir='.'

file = '+50C(2).csv'

files_in_dir = os.listdir(current_dir)

if file in files_in_dir:
    print("OK")

slected_colums = []

headers = ['Время','T1','T2','T3','T4','T5','T6']

df = pd.read_csv("+50C(2).csv",sep="\t" ,header=None,names=headers, dtype=float)

df.info()

#df["T5-T2"] = df["T5"] - df["T2"]
#print (df['Время'])