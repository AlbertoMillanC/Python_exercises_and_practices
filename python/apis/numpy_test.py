
from itertools import product
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


data = [[23, 36, 15, 18, 56, 45, 32, 10, 43, 55, 41, 63, 12], ["Jaunary ", "February ", "March ", "April ", "May ", "June ", "July ", "August ", "September ", "October ", "November ", "December ", "Total"]]
                                                              
# average in each month

def new_func(data):
    df = pd.DataFrame(data, index=list("PM"))
    produces = df.iloc[0, :]
    print(df)
    return df,produces

df, produces = new_func(data)
# calculate the average
average = np.mean(produces)
print("the company's produces average was", average)

# higher production .
def new_func1(df):
    dfT = df.transpose()
    print(dfT)
    maxi = dfT.max()
    return dfT,maxi

dfT, maxi = new_func1(df)

def new_func2(dfT, maxi):
    np.where(dfT == maxi)
    greater_than = np.where(dfT == maxi)
    P = (greater_than[0][1])
    return P

P = new_func2(dfT, maxi)

print("the produces greater than ", df[P][0], "and it occurred in the month Total", df[P][1])

# semestre de menor produces.
semester_period_1 = produces.head(6).sum()
print("the produces del semester period one was ", semester_period_1)
semester_period_2 = produces.tail(6).sum()
print("the produces of the semester period two was  ", semester_period_2)


#months where more than 50 airs occurreddfT 
   

dfT[dfT["P"] > 50]

# average odd months

averageI = dfT.iloc[[0, 1, 3, 5, 7, 9, 11], [0]].mean()
print("average odd months", averageI)

# months where production exceeded the average

prome_P= dfT["P"].mean()
dfT[dfT["P"] > prome_P]

# graphic
plt.plot(dfT["P"], dfT["M"])
