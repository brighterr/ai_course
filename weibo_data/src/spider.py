import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin

# 目标网站的URL
url = 'http://portal.misc.pullword.com:40001/bangdan/'

# 创建一个文件夹以保存下载的文档
os.makedirs('downloaded_docs', exist_ok=True)

# 发送请求
response = requests.get(url)
response.raise_for_status()  # 检查请求是否成功

# 解析HTML
soup = BeautifulSoup(response.text, 'html.parser')

# 找到所有文档链接
for link in soup.find_all('a', href=True):
    href = link['href']
    
    # 检查链接是否以"weibo_bangdan"开头
    if href.startswith("weibo_bangdan"):
        doc_url = urljoin(url, href)  # 使用urljoin处理相对路径
        print(f"Downloading: {doc_url}")
        
        try:
            # 下载文档
            doc_response = requests.get(doc_url)
            doc_response.raise_for_status()  # 检查请求是否成功

            # 保存文档
            filename = os.path.join('downloaded_docs', os.path.basename(href))
            with open(filename, 'wb') as f:
                f.write(doc_response.content)
            print(f"Saved: {filename}")
        except requests.HTTPError as e:
            print(f"Failed to download {doc_url}: {e}")

print("所有文档已下载。")
