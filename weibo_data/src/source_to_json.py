import json
import re
import pandas as pd 
import numpy as np
import csv
import sys

def parse_file(input_file_name,output_file_name):


    # 存储 JSON 对象的列表
    json_objects = []

    # 读取文件
    with open(input_file_name, 'r', encoding='utf-8') as input_file:
        for line in input_file:  # 按行读取
            index = line.find('{')  # 查找第一个 '{'
            if index != -1:  # 如果找到了 '{'
                cleaned_line = line[index:]  # 清理行，保留 '{' 及其后的内容
                try:
                    # 尝试解析 JSON
                    dictionary = json.loads(cleaned_line)
                    bangdan_data = json.loads(dictionary['bangdan'])
                    cards_data = bangdan_data.get("cards",None)
                    json_objects.append(cards_data)  # 添加到列表
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON: {e}")  # 错误处理

    # 将结果保存为 JSON 文件
    with open(output_file_name, 'w', encoding='utf-8') as output_file:
        json.dump(json_objects, output_file, ensure_ascii=False, indent=4)

    print(f"Parsed {len(json_objects)} JSON objects and saved to {output_file_name}.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("用法: python source_to_json.py <input_file>")
    else:
        input_file_name = sys.argv[1]
        output_file_name = sys.argv[2]
        parse_file(input_file_name,output_file_name)

"""
input_file_name = 'weibo_bangdan.2024-01-01'
output_file_name = input_file_name + '.json'

# 存储 JSON 对象的列表
json_objects = []

# 读取文件
with open(input_file_name, 'r', encoding='utf-8') as input_file:
    for line in input_file:  # 按行读取
        index = line.find('{')  # 查找第一个 '{'
        if index != -1:  # 如果找到了 '{'
            cleaned_line = line[index:]  # 清理行，保留 '{' 及其后的内容
            try:
                # 尝试解析 JSON
                dictionary = json.loads(cleaned_line)
                bangdan_data = json.loads(dictionary['bangdan'])
                cards_data=bangdan_data['cards']
                json_objects.append(cards_data)  # 添加到列表
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")  # 错误处理

# 将结果保存为 JSON 文件
with open(output_file_name, 'w', encoding='utf-8') as output_file:
    json.dump(json_objects, output_file, ensure_ascii=False, indent=4)

print(f"Parsed {len(json_objects)} JSON objects and saved to {output_file_name}.")






# 查找所有匹配项
matches = re.findall(pattern, data, re.DOTALL)
print(len(matches))
# 将匹配的 JSON 字符串转换为字典
json_objects = []
for number, json_content in matches:
    try:
        # 解析 JSON
        json_content_with_braces = f'{{ {json_content} }}'
        json_obj = json.loads(json_content_with_braces)  # 解析 JSON
        json_obj['id'] = number  # 将数字作为 id 添加
        json_objects.append(json_obj)  # 添加到结果列表
    except json.JSONDecodeError as e:
        print(f"JSONDecodeError: {e} for content: {json_content}")

# 打印结果
for json_obj in json_objects:
    print(json.dumps(json_obj, ensure_ascii=False, indent=2))
    
with open(output_file_name, 'w', encoding='utf-8') as output_file:
    json.dump(json_objects, output_file, ensure_ascii=False, indent=2)

print(f"数据已保存到 {output_file_name}")
"""