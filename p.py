import requests

proxies = {
    "http": "socks5h://user:pass@bdix.bypassempire.com:1080",
    "https": "socks5h://user:pass@bdix.bypassempire.com:1080",
}

try:
    r = requests.get('https://www.google.com', proxies=proxies, timeout=10)
    print("Proxy connection success:", r.status_code)
except Exception as e:
    print("Proxy connection failed:", e)
