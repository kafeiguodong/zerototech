import requests

# 禁用代理，并添加超时时间
resp = requests.get(
    "http://localhost:8000/api/profile",
    timeout=5,  # 5秒超时
    proxies={"http": None, "https": None}  # 绕过代理
)
print(resp.json())