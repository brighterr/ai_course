import os
import py7zr

# 定义文件夹路径
downloaded_docs_folder = 'downloaded_docs'
output_folder = 'data/raw'

# 创建输出文件夹（如果不存在）
os.makedirs(output_folder, exist_ok=True)

# 遍历 downloaded_docs 文件夹中的所有 .7z 文件
for filename in os.listdir(downloaded_docs_folder):
    if filename.startswith('weibo_bangdan.') and filename.endswith('.7z'):
        file_path = os.path.join(downloaded_docs_folder, filename)
        # 解压到 output_folder
        with py7zr.SevenZipFile(file_path, mode='r') as archive:
            archive.extractall(path=output_folder)
        print(f"解压: {filename} 到 {output_folder}")

print("所有文件已成功解压。")