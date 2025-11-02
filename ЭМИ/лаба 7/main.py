#import pandas as pd
import csv

#file_path = 'C:\Users\andre\OneDrive\Desktop\MPEI\ЭМИ\лаба 7\+50C(2).csv'

slected_colums = []

df = pd.read_csv("C:\Users\\andre\\OneDrive\\Desktop\\MPEI\\ЭМИ\\лаба 7\\+50C(2).csv", header=None)

df.columns = ['Время','T1','T2','T3','T4','T4','T5','T6']

print (df)