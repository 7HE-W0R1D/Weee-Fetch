import requests
import json
import time
import csv
import os

try:
    from tqdm import tqdm
except ImportError:
    print("缺少必要的库，请在终端运行: pip install tqdm")
    exit()

# 引入公共请求头工具
import weee_headers

def fetch_all_reviews(product_id, max_pages=2, lang='zh'):
    base_url = "https://api.sayweee.net/ec/social/review"
    all_reviews = []
    page = 1
    limit = 20
    
    with tqdm(total=max_pages, desc="Fetching review pages", unit="page") as pbar:
        while page <= max_pages:
            params = {
                "product_id": product_id,
                "sort": "relevance",
                "page": page,
                "limit": limit
            }
            
            try:
                response = requests.get(base_url, params=params, headers=weee_headers.get_headers(product_id, lang))
                data = response.json()
                
                # 根据实际返回结构提取评论列表
                object_data = data.get('object') or {}
                reviews = object_data.get('list', [])
                
                if not reviews:
                    break
                    
                all_reviews.extend(reviews)
                
                page += 1
                pbar.update(1)
                # 稍微停顿一下，避免请求过快被封禁
                time.sleep(1) 
                
            except Exception as e:
                pbar.write(f"Error at page {page}: {e}")
                break
                
    return all_reviews

# 开始抓取
import argparse

parser = argparse.ArgumentParser(description='Fetch Weee reviews (2p)')
parser.add_argument('--product-id', default='27605', help='Product ID to fetch')
parser.add_argument('--lang', default='zh', choices=['zh', 'en'], help='Language (zh or en)')
args = parser.parse_args()
product_id = args.product_id
lang = args.lang

# 直接使用提供的 product_id，无需解析 URL
data = fetch_all_reviews(product_id, lang=lang)

current_time = time.strftime("%Y%m%d_%H%M%S")
num_reviews = len(data)
base_name = f"{product_id}_{current_time}_{num_reviews}"
base_dir = os.path.join("fetched-data", base_name)

if not os.path.exists(base_dir):
    os.makedirs(base_dir)

json_filename = os.path.join(base_dir, f"{base_name}.json")
csv_filename = os.path.join(base_dir, f"{base_name}.csv")

# 保存为JSON文件
with open(json_filename, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

# 保存为CSV文件
if data:
    with open(csv_filename, "w", encoding="utf-8", newline="") as f:
        # 提取所有的列名，保持字段顺序
        fieldnames = []
        for review in data:
            for key in review:
                if key not in fieldnames:
                    fieldnames.append(key)
        
        # 格式化特殊字段（去除列表自带的括号，直接显示链接）
        csv_data = []
        for review in tqdm(data, desc="Processing CSV rows"):
            row = dict(review)
            if isinstance(row.get('pictures'), list):
                row['pictures'] = ", ".join(str(p) for p in row['pictures'])
            csv_data.append(row)
        
        # 写入CSV
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(csv_data)

print(f"Downloaded reviews from the first 2 pages have been saved to {json_filename} and {csv_filename}")
