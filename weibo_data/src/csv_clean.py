import pandas as pd
import re
import sys
import os

def clean_csv(input_file_path,output_folder):
    # 读取 CSV 文件
    df = pd.read_csv(input_file_path)

    # 提取 "热度" 列中的数字
    df['热度'] = df['热度'].astype(str).str.extract('(\d+)')

    # 去除没有热度数字的行
    df = df.dropna(subset=['热度'])

    # 转换 "热度" 列为数值类型
    df['热度'] = pd.to_numeric(df['热度'], errors='coerce')

    # 根据 "热搜词条" 计算平均热度并去重
    average_heat = df.groupby('热搜词条', as_index=False)['热度'].mean()

    # 将平均热度取整
    average_heat['热度'] = average_heat['热度'].round().astype(int)

    # 确定输出文件名
    output_file_name = os.path.join(output_folder, os.path.basename(input_file_path))

    # 保存结果到新的 CSV 文件
    average_heat.to_csv(output_file_name, index=False, encoding='utf-8')
    print(f"平均热度计算完成，已保存至 {output_file_name}")
if __name__ == "__main__":
    # 检查命令行参数
    if len(sys.argv) != 3:
        print("用法: python csv_clean.py <input_json_file> <output_>")
    else:
        input_file_name = sys.argv[1]
        output_folder_name = sys.argv[2]
        clean_csv(input_file_name,output_folder_name)
"""
# 读取 CSV 文件
file_name='weibo_bangdan.2024-01-01'
output_file_name = 'weibo_bangdan.2024-01-01.csv'

df = pd.read_csv(output_file_name)

# 提取 "热度" 列中的数字
df['热度'] = df['热度'].astype(str).str.extract('(\d+)')

# 去除没有热度数字的行
df = df.dropna(subset=['热度'])

# 转换 "热度" 列为数值类型
df['热度'] = pd.to_numeric(df['热度'])

# 根据 "热搜词条" 计算平均热度并去重
average_heat = df.groupby('热搜词条', as_index=False)['热度'].mean()

# 将平均热度取整
average_heat['热度'] = average_heat['热度'].round().astype(int)

# 保存结果到新的 CSV 文件
average_heat.to_csv(output_file_name, index=False)
average_heat.to_excel('20240101.xlsx', index=False)
print("平均热度计算完成，已取整并保存至新 CSV 文件。")
###
"""