import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# 选择一个特定的热搜词条
target_keyword = '时代少年团'  # 替换为你要可视化的热搜词条
combined_df = pd.read_csv("./data/processed/总表.csv")

# 筛选出包含该热搜词条的数据
keyword_data = combined_df[combined_df['热搜词条'].str.contains(target_keyword, na=False)]

# 确保日期列为 datetime 格式
keyword_data['日期'] = pd.to_datetime(keyword_data['日期'])

# 按日期分组并求和
daily_data = keyword_data.groupby('日期', as_index=False)['热度'].sum()

# 重置索引以便于绘图
daily_data.reset_index(drop=True, inplace=True)

# 创建可视化
plt.figure(figsize=(12, 6))
sns.lineplot(data=daily_data, x='日期', y='热度', marker='o')

# 设置标题和标签
plt.title(f"Hot Trends", fontsize=16)  # 图形标题
plt.xlabel("Date", fontsize=14)  # x 轴标签
plt.ylabel("Total Hot", fontsize=14)  # y 轴标签

# 选择均匀分布的 x 轴刻度
num_xticks = min(12, len(daily_data))  # 确保不超过10个刻度
xticks_indices = np.linspace(0, len(daily_data) - 1, num_xticks).astype(int)  # 选择均匀分布的索引
xticks = daily_data['日期'].iloc[xticks_indices]  # 获取对应的日期
plt.xticks(xticks, rotation=45)  # 设置刻度并旋转

plt.grid()
plt.tight_layout()

# 保存图形到文件
output_file = './img/' + target_keyword + '热度变化' + '.png'  # 指定保存路径
plt.savefig(output_file)  # 保存图形
plt.close()  # 关闭当前图形，以释放内存

print(f"图形已保存至 {output_file}")
