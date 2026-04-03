import requests
import json
import os
import time
try:
    from tqdm import tqdm
except ImportError:
    print("缺少必要的库，请在终端运行: pip install tqdm")
    exit()

def fetch_weee_reviews_cn(product_id, limit=20):
    """
    专门针对中文评论优化的抓取函数
    """
    base_url = "https://api.sayweee.net/ec/social/review"
    
    # 核心：模拟中文浏览器的请求头
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8", # 告诉服务器优先返回中文
        "lang": "zh",
        "Referer": f"https://www.sayweee.com/zh/product/view/{product_id}"
    }
    
    all_reviews = []
    page = 1
    
    # 模拟网页上的 excluded_ids (可选，通常用于分页去重)
    # 默认我们可以不传，抓取更全的数据
    
    print(f"\n🚀 正在开始尝试抓取商品 {product_id} 的中文评论...")
    
    with tqdm(desc="抓取进度", unit="页") as pbar:
        while True:
            params = {
                "product_id": product_id,
                "sort": "relevance",  # 按相关性（中文评论通常更靠前）
                "page": page,
                "limit": limit
            }
            
            try:
                response = requests.get(base_url, params=params, headers=headers)
                response.raise_for_status()
                data = response.json()
                
                # 获取评论列表
                object_data = data.get('object', {})
                reviews = object_data.get('list', [])
                
                if not reviews:
                    break
                    
                all_reviews.extend(reviews)
                pbar.update(1)
                
                # 第一次请求时，输出总评论数
                if page == 1:
                    total = object_data.get('total', '未知')
                    pbar.write(f"💡 该商品在数据库共有 {total} 条评论")
                
                # 为了演示，我们只抓取前 3 页
                if page >= 3: 
                    pbar.write("\n✅ 测试阶段：已抓取前 3 页数据。")
                    break
                
                page += 1
                time.sleep(1) # 礼貌间隔
                
            except Exception as e:
                pbar.write(f"❌ 抓取第 {page} 页时发生错误: {e}")
                break
                
    return all_reviews

if __name__ == "__main__":
    # 使用你提供的商品 ID: 58583 (青葱)
    TARGET_PRODUCT_ID = "58583"
    
    reviews_data = fetch_weee_reviews_cn(TARGET_PRODUCT_ID)
    
    # 创建保存目录
    save_dir = "fetched-data/cn_test"
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
        
    current_time = time.strftime("%Y%m%d_%H%M%S")
    file_name = f"reviews_{TARGET_PRODUCT_ID}_{current_time}.json"
    file_path = os.path.join(save_dir, file_name)
    
    # 保存结果
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(reviews_data, f, ensure_ascii=False, indent=4)
        
    print(f"\n🎉 抓取完成！共获得 {len(reviews_data)} 条评论。")
    print(f"📁 结果已保存至: {file_path}")
    
    # 打印前两条预览，验证中文
    if reviews_data:
        print("\n📝 --- 抓取结果预览 ---")
        for i, r in enumerate(reviews_data[:3]):
            print(f"[{i+1}] 用户: {r.get('user_name')} | 评分: {r.get('rating')}")
            # comment 字段通常是原文
            print(f"    原始文本: {r.get('comment')}")
            # 如果有翻译，Weee 会放在 comment_lang 或者 comment 里
            print(f"    显示文本: {r.get('comment_lang')}")
            print("-" * 30)
