import pandas as pd
xl1 = 'wk1-all.xlsx'
xl2 = 'quesbank.xlsx'

dataframe1 = pd.read_excel(xl1)
df2 = pd.read_excel(xl2)

merge = pd.merge(df1, df2, on="column name")

print(merge)

merge.to_excel("output.xlsx")
