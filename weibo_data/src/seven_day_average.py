import pandas as pd
import glob
import os
import re

# 设置文件夹路径
folder_path = './data/processed/'  # 替换为你的文件夹路径

# 创建一个空的列表来存储数据框
dataframes = []

# 使用glob获取所有符合格式的CSV文件
file_pattern = os.path.join(folder_path, 'weibo_bangdan.*.csv')
files = glob.glob(file_pattern)
print(f"找到 {len(files)} 个文件")

# 读取每个文件并添加到列表中
for file in files:
    try:
        # 提取文件名中的日期（假设日期格式为 YYYY-MM-DD）
        date_match = re.search(r'(\d{4}-\d{2}-\d{2})', os.path.basename(file))
        if date_match:
            date = date_match.group(1)
            # 读取CSV文件，假设包含 '热搜词条', '热度' 列
            df = pd.read_csv(file, header=0, names=['热搜词条', '热度'], skiprows=1)
            df['日期'] = pd.to_datetime(date)
            dataframes.append(df)
    except Exception as e:
        print(f"读取文件 {file} 时出错: {e}")

# 合并所有数据框
if dataframes:
    combined_df = pd.concat(dataframes, ignore_index=True)

    # 设置日期为索引
    combined_df.set_index('日期', inplace=True)

    # 确保每个热搜词条的索引是单调递增的
    combined_df.sort_values(by=['热搜词条', '日期'], inplace=True)

    # 计算七日平均热度
    seven_day_avg = combined_df.groupby('热搜词条')['热度'].rolling(window='7D').mean().reset_index()
    seven_day_avg =seven_day_avg.sort_values(by="热度",ascending=False)
    # 将结果存入Excel文件
    output_file = os.path.join(folder_path, '七日平均热度统计.xlsx')
    seven_day_avg.to_excel(output_file, index=False)

    print(f"结果已保存到 {output_file}")
else:
    print("没有找到任何有效的CSV文件。")
