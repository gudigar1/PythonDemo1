import pandas as pd
import numpy as np
#C:\Users\om\Downloads\Automobile_data.csv

print('Hello World')
df=pd.read_csv(r"C:\Users\om\Downloads\Automobile_data.csv")
print(df.head(50))
print(df.size)
print('---------------------------------------------------------------------------------------------------')
print('#1')
df1=df.drop(range(40,45))
print(df1.head(50))
print('---------------------------------------------------------------------------------------------------')
print('#2')
df2=pd.DataFrame(df)
index_names=df2[(df2['company']=='toyota')&(df2['body-style']=='wagon')].index
df2.drop(index_names,inplace=True)
print(df2.head(60))
print('---------------------------------------------------------------------------------------------------')
print('#3')
df['price'].fillna(500,inplace=True)
print(df.head(30))
print('---------------------------------------------------------------------------------------------------')
print('#4')
df3=(df.groupby('company').count())
print(df3.head(20))
print('---------------------------------------------------------------------------------------------------')
print('#5')
df4=df.sort_values(by='price')
print(df4.head(20))
print('---------------------------------------------------------------------------------------------------')
print('#6')
def dis_price(x):
    return x*0.9
df5=pd.DataFrame(df)
df5['discount_price']=df['price'].transform(dis_price)
print(df5.head(10))
print('---------------------------------------------------------------------------------------------------')
print('#7')
dict={'three':'3','four':'4','five':'5','six':'6','eight':'8','twelve':'12'}
df=df.replace({'num-of-cylinders':dict})
print(df['num-of-cylinders'].head())
print('---------------------------------------------------------------------------------------------------')