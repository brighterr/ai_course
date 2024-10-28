import os
import subprocess
from datetime import datetime, timedelta

# 定义文件夹路径
raw_data_folder = './data/raw'
processed_data_folder = './data/processed'

# 确保 processed 文件夹存在
os.makedirs(processed_data_folder, exist_ok=True)

# 定义起始和结束日期
start_date = datetime(2024, 9, 23)
end_date = datetime(2024, 10, 22)

# 生成日期范围内的文件名（不带 .7z 后缀）
date_list = [(start_date + timedelta(days=i)).strftime('%Y-%m-%d') for i in range((end_date - start_date).days + 1)]
file_names = [f"weibo_bangdan.{date}" for date in date_list]

# 依次处理每个文件
for filename in file_names:
    raw_file_path = os.path.join(raw_data_folder, filename)

    # 检查文件是否存在
    if os.path.isfile(raw_file_path):
        print(f"处理文件: {filename}")

        # 运行 source_to_json.py
        json_file_path = os.path.join(raw_data_folder, filename + '.json')
        subprocess.run(['python', 'source_to_json.py', raw_file_path, json_file_path])

        # 运行 json_to_csv.py，并提供输入输出文件名
        csv_file_path = os.path.join(raw_data_folder, filename + '.csv')
        subprocess.run(['python', 'json_to_csv.py', json_file_path, csv_file_path])

        # 运行 csv_clean.py，并提供输入输出文件名
        subprocess.run(['python', 'csv_clean.py', csv_file_path, processed_data_folder])
        if os.path.isfile(json_file_path):
            os.remove(json_file_path)
        if os.path.isfile(csv_file_path):
            os.remove(csv_file_path)
        #os.remove(csv_file_path)
    else:
        print(f"文件未找到: {filename}")

print("所有文件处理完成。")
