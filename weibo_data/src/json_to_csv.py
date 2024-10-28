import json
import re
import pandas as pd 
import numpy as np
import csv
import sys

def json_to_csv(input_file_name, output_file_name):
    pattern = r'"desc"\s*:\s*"([^"]*)",\s*"desc_extr"\s*:\s*"([^"]*)"'

    with open(input_file_name, 'r', encoding='utf-8') as input_file:
        dirty_data = input_file.read()
    #json_data=json.loads(dirty_data)
    #result_string = json.dumps(json_data, ensure_ascii=False)
    def find_matches(text, pattern):
        matches = re.findall(pattern, text)
        return matches

    results = find_matches(dirty_data, pattern)
    if results:
        df = pd.DataFrame(results, columns=['热搜词条', '热度'])
        df.to_csv(output_file_name, index=False, encoding='utf-8')
        print(f"CSV 文件 '{output_file_name}' 创建成功。")
    else:
        print("未找到匹配项。")

if __name__ == "__main__":
    # 检查命令行参数
    if len(sys.argv) != 3:
        print("用法: python json_to_csv.py <input_json_file> <output_csv_file>")
    else:
        input_file_name = sys.argv[1]
        output_file_name = sys.argv[2]
        json_to_csv(input_file_name, output_file_name)

"""
input_file_name ='weibo_bangdan.2024-01-01.json'
output_file_name ='weibo_bangdan.2024-01-01.csv'
pattern = r'"desc"\s*:\s*"([^"]*)",\s*"desc_extr"\s*:\s*"([^"]*)"'
with open(input_file_name, 'r', encoding='utf-8') as input_file:
    json_data=input_file.read()
def find_matches(text, pattern):
    matches = re.findall(pattern, text)
    return matches
results = find_matches(json_data, pattern)
if results:
    df = pd.DataFrame(results, columns=['热搜词条', '热度'])
    df.to_csv(output_file_name, index=False, encoding='utf-8')
    print("CSV 文件创建成功。")
else:
    print("未找到匹配项。")
"""