import pandas as pd
df1 = pd.read_csv('bigram1.csv')
df2 = pd.read_csv('bigram2.csv')
df3 = pd.concat([df1, df2]).groupby(['gram1','gram2']).sum()
df3.to_csv('merged_bigram.csv')