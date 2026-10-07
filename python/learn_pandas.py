import pandas as pd
df=pd.read_csv('scores.csv')
print(df)
print(df.head(),'\n')
print(df.tail())
print(df.shape)
print(df.iloc[0,0],'\n')
df.info()
print('info:\n',df.info())
print('discribe:\n',df.describe(),'\n')
df['分数加1']=df['分数']+1
print(df['分数'].shape)
print(df[['分数']].shape)
try:
    print(df['分数','分数加1'].shape)
except KeyError as e:
    print("KeyError:",e)    
print(df[['分数','分数加1']].shape)
df['分数']=df['分数']*2
print('discribe:\n',df.describe(),'\n')
print(df[(df['分数加1'].between(20,80))])
print(df[(df['分数加1']>70)|(df['分数']<100)])


df1=pd.DataFrame({
    '姓名':['张三','李四','王五','赵六','钱七','孙八'],
    '城市':['A','B','C','A','B','A'],
    '分数':[53,56,66,95,85,90],
    '年龄':[24,14,56,34,56,34]
},index=['A','B','C','D','E',"F"])
print(df1.groupby('城市')['分数'].sum())
try:
    print(df1.groupby('城市')['分数','年龄'].shape)
except ValueError as e:
    print('ValueError:',e)
print(df1.groupby('城市')[['分数','年龄']].sum())
print(df1.groupby('城市')[['分数','年龄']].sum().shape)

print(df1.loc['A'])
print(df1.iloc[0])
print(df1['分数'].idxmax())