import pandas as pd

df_dict={'a':['1','2'],
        'b':['3','4'],
        'c':['5','6']}

df=pd.DataFrame.from_dict(df_dict)
print(df)