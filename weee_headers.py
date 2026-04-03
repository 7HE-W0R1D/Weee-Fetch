def get_headers(product_id: str, lang: str = "zh") -> dict:
    """Return request headers for Weee! API.
    Args:
        product_id: The product ID being queried.
        lang: Language code, "zh" for Chinese (default) or "en" for English.
    """
    # User-Agent mimics a modern Chrome browser on macOS
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    # Accept-Language based on requested language
    if lang == "zh":
        accept_language = "zh-CN,zh;q=0.9,en;q=0.8"
        referer = f"https://www.sayweee.com/zh/product/view/{product_id}"
    else:
        accept_language = "en-US,en;q=0.9,zh;q=0.8"
        referer = f"https://www.sayweee.com/en/product/view/{product_id}"
    return {
        "User-Agent": user_agent,
        "Accept-Language": accept_language,
        "lang": lang,
        "Referer": referer,
    }
