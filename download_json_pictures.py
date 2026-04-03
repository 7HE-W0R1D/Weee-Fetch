import json
import os
import requests
import sys

try:
    from tqdm import tqdm
except ImportError:
    print("缺少必要的库，请在终端运行: pip install tqdm")
    exit()

def download_pictures_from_json(json_path):
    # 去除路径里可能携带的多余引号
    json_path = json_path.strip('"\'')
    
    if not os.path.exists(json_path):
        print(f"找不到文件: {json_path}")
        return

    # 解析保存文件夹名字，和 json 文件同名
    base_name = os.path.splitext(os.path.basename(json_path))[0]
    output_dir = os.path.join(os.path.dirname(os.path.abspath(json_path)), base_name)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"创建了文件夹: {output_dir}")

    # 读取 JSON 数据
    with open(json_path, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            print(f"无法解析 JSON 文件: {json_path}")
            return

    if not isinstance(data, list):
        print("JSON 格式不是期待的列表结构 (Weee-Fetch 的格式)。")
        return

    print(f"开始解析文件: {json_path}，共有 {len(data)} 条评价。")
    
    total_images = sum(1 for review in data if isinstance(review.get('pictures'), list) for _ in review.get('pictures'))
    if total_images == 0:
        print("没有找到需要下载的图片。")
        return
        
    print(f"准备下载 {total_images} 张高清图片...")
    
    total_downloaded = 0
    with tqdm(total=total_images, desc="Downloading images", unit="img") as pbar:
        for review_idx, review in enumerate(data, start=1):
            pictures = review.get('pictures')
            if not pictures or not isinstance(pictures, list):
                continue
    
            review_id = review.get('id', review_idx)
    
            for pic_idx, img_url in enumerate(pictures, start=1):
                if img_url.startswith('//'):
                    img_url = 'https:' + img_url
    
                # 根据URL推断扩展名，如果未能获取则默认用 .jpg
                ext = os.path.splitext(img_url.split('?')[0])[-1]
                if ext.lower() not in ['.jpg', '.jpeg', '.png', '.gif', '.webp']:
                    ext = '.jpg'
                    
                # 命名格式: 评论ID_图片序号.后缀
                filename = f"{review_id}_{pic_idx}{ext}"
                filepath = os.path.join(output_dir, filename)
    
                try:
                    response = requests.get(img_url, timeout=10)
                    if response.status_code == 200:
                        with open(filepath, 'wb') as img_f:
                            img_f.write(response.content)
                        total_downloaded += 1
                    else:
                        print(f"\n下载失败: {img_url} (状态码: {response.status_code})")
                except Exception as e:
                    print(f"\n下载出错 {img_url}: {e}")
                    
                pbar.update(1)

    print(f"\n全部完成！共下载了 {total_downloaded} 张高清图片到文件夹: {output_dir}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        json_file = " ".join(sys.argv[1:])
    else:
        json_file = input("请输入要解析提取图片的 JSON 文件名或路径 (例如 27605_xxx.json): ").strip()
        
    if json_file:
        download_pictures_from_json(json_file)
    else:
        print("未输入有效文件路径，退出。")
