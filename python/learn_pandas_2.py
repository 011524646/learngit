import pandas as pd
df=pd.read_csv('scores_raw.csv')
df1=pd.DataFrame({
    '班级':['一班','二班','三班','四班'],
    '班主任':['A','B','C','D']
})
df.isna()
print("===== 1. 缺失值分布 =====")
df[df['语文'].isna()]
print(df.fillna('缺考'))
print(df.replace('缺考',0))

print("\n===== 2. 重复行 =====")
print("重复行数：", df.duplicated().sum())
print(df[df.duplicated(keep=False)])
clean = df.drop_duplicates()

print("\n===== 3. 去重前后 =====")
print("原始：", df.shape, " → 去重后：", clean.shape)

print("\n===== 5. 性别+班级 两层分组 =====")
test1=df.groupby(['性别','班级'])['语文'].agg(['mean'])
test2=df.groupby(['性别','班级'])['语文'].agg(['mean'])
print("[性别,班级]"); print(test1)
print("\n[班级,性别]"); print(test2)