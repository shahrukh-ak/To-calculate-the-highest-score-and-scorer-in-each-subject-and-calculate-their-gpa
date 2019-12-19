import pandas as pd
import numpy as np
from pandas import DataFrame

df = pd.read_csv('records.txt')

df.loc[df['ece595'] >= 90, 'Grade-ece595'] = 'A'
df.loc[(df['ece595'] <= 89) & (df['ece595'] >= 80), 'Grade-ece595'] = 'B'
df.loc[(df['ece595'] <= 79) & (df['ece595'] >= 70), 'Grade-ece595'] = 'C'
df.loc[(df['ece595'] <= 69) & (df['ece595'] >= 60), 'Grade-ece595'] = 'D'
df.loc[df['ece595'] <= 59, 'Grade-ece595'] = 'F'


#####################################################################
df.loc[df['ece547'] >= 90, 'Grade-ece547'] = 'A'
df.loc[(df['ece547'] <= 89) & (df['ece547'] >= 80), 'Grade-ece547'] = 'B'
df.loc[(df['ece547'] <= 79) & (df['ece547'] >= 70), 'Grade-ece547'] = 'C'
df.loc[(df['ece547'] <= 69) & (df['ece547'] >= 60), 'Grade-ece547'] = 'D'
df.loc[df['ece547'] <= 59, 'Grade-ece547'] = 'F'



#####################################################################
df.loc[df['ece354'] >= 90, 'Grade-ece354'] = 'A'
df.loc[(df['ece354'] <= 89) & (df['ece354'] >= 80), 'Grade-ece354'] = 'B'
df.loc[(df['ece354'] <= 79) & (df['ece354'] >= 70), 'Grade-ece354'] = 'C'
df.loc[(df['ece354'] <= 69) & (df['ece354'] >= 60), 'Grade-ece354'] = 'D'
df.loc[df['ece354'] <= 59, 'Grade-ece354'] = 'F'



####  HIGHEST SCORE  #####
a = df['ece595'].max()
b = df['ece547'].max()
c = df['ece354'].max()
print(a)
print(b)
print(c)


####  HIGHEST SCORER  #####
x = df[df['ece595'] == a]
y = df[df['ece547'] == b]
z = df[df['ece354'] == c]
print(x)
print(y)
print(z)

####  GPA of each student  ####
df.loc[(df['Grade-ece595'] == 'A'), 'Grade Points-ece595'] = 4
df.loc[(df['Grade-ece595'] == 'B'), 'Grade Points-ece595'] = 3
df.loc[(df['Grade-ece595'] == 'C'), 'Grade Points-ece595'] = 2
df.loc[(df['Grade-ece595'] == 'D') , 'Grade Points-ece595'] = 1
df.loc[(df['Grade-ece595'] == 'F'),'Grade Points-ece595'] = 0



####################################
df.loc[(df['Grade-ece547'] == 'A'), 'Grade Points-ece547'] = 4
df.loc[(df['Grade-ece547'] == 'B'), 'Grade Points-ece547'] = 3
df.loc[(df['Grade-ece547'] == 'C'), 'Grade Points-ece547'] = 2
df.loc[(df['Grade-ece547'] == 'D') , 'Grade Points-ece547'] = 1
df.loc[(df['Grade-ece547'] == 'F'),'Grade Points-ece547'] = 0




####################################
df.loc[(df['Grade-ece354'] == 'A'), 'Grade Points-ece354'] = 4
df.loc[(df['Grade-ece354'] == 'B'), 'Grade Points-ece354'] = 3
df.loc[(df['Grade-ece354'] == 'C'), 'Grade Points-ece354'] = 2
df.loc[(df['Grade-ece354'] == 'D') , 'Grade Points-ece354'] = 1
df.loc[(df['Grade-ece354'] == 'F'),'Grade Points-ece354'] = 0


credit_hour = 3
sum_of_credit_hours = 3*3
df["Sum of credit hours * grade points"] = ( credit_hour * df["Grade Points-ece595"]) + (credit_hour * df["Grade Points-ece547"]) + (credit_hour * df["Grade Points-ece354"]) 


df["GPA"] = df["Sum of credit hours * grade points"] // sum_of_credit_hours




