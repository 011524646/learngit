import pandas as pd
from pathlib import Path
import matplotlib
matplotlib.use('Agg')                      # ← 必须在 import pyplot 之前
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False

##数据导入
BASE = Path(__file__).parent
df   = pd.read_csv(BASE / 'scores_raw.csv')
temp = pd.read_csv(BASE / 'class.csv')
df=pd.merge(df,temp,on='班级',how='inner')


#清洗
print(df.isna().shape)
print(df.isna().sum())
df=df.drop_duplicates(subset=['学号'])
df=df.dropna(subset=['数学','语文','英语'])
print(df)

#统计
t = df.groupby('班级')[['语文','数学','英语']].mean().round(2)
print(t)
# ---- 出图 ----
print("\n===== 出图 =====")
# 图1：各班各科均分
fig, ax = plt.subplots(figsize=(7, 4))
t.plot(kind='bar', ax=ax)
ax.set_title('各班各科平均分')
ax.set_xlabel('班级')
ax.set_ylabel('平均分')
ax.tick_params(axis='x', rotation=0)
ax.legend(title='科目')
ax.grid(axis='y', alpha=0.3)
fig.tight_layout()
fig.savefig(BASE / 'chart1.png', dpi=110)
plt.close(fig)

# 图2：三科分布
fig, ax = plt.subplots(figsize=(7, 4))
df[['语文','数学','英语']].plot(kind='box', ax=ax)
ax.set_title('三科成绩分布')
ax.set_ylabel('分数')
ax.grid(axis='y', alpha=0.3)
fig.tight_layout()
fig.savefig(BASE / 'chart2.png', dpi=110)
plt.close(fig)

print("已生成 chart1.png / chart2.png")