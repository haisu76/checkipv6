from urllib.parse import urlparse
import urllib3
import socket
import argparse

import requests
# 禁止https请求不验证证书时产生警告信息
requests.packages.urllib3.disable_warnings()

def allowed_gai_family():
    # AF_INET表示IPv4地址族，AF_INET6表示IPv6地址族
    return socket.AF_INET6

# 重写allowed_gai_family方法，设置ip地址族为ipv6
urllib3.util.connection.allowed_gai_family = allowed_gai_family

def ipv6_access_check(url):
    # 首先获取域名AAAA解析地址，也就是ipv6地址
    aaaa = ""
    try:
        # 解析出url的域名
        domain = urlparse(url).hostname
        # socket.getaddrinfo返回结果示例：
        # [(<AddressFamily.AF_INET6: 23>, 0, 0, '', ('240e:c1:6800::19', 0, 0, 0)), (<AddressFamily.AF_INET6: 23>, 0, 0, '', ('240e:780:4000:1::7', 0, 0, 0))]
        aaaa = socket.getaddrinfo(domain, None, socket.AF_INET6)[0][4][0]
    # 如果出现异常，说明不支持ipv6访问，返回False
    except Exception as e:
        pass
    if aaaa == "":
        print(f"{url}不支持ipv6访问，不支持解析AAAA地址。")
        return False
    # 检查ipv6网站是否可访问
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.41"}
    try:
        r = requests.get(url, timeout=3, verify=False, headers=headers)
        code = r.status_code
    except Exception as e:
        code = -1
    if code == 200:
        print(f"{url}支持ipv6访问，解析AAAA地址为：{aaaa}，响应状态码为：{code}。")
        return True
    else:
        print(f"{url}不支持ipv6访问，解析AAAA地址为：{aaaa}，响应状态码为：{code}。")
        return False 

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="检测URL是否支持IPv6访问")
    parser.add_argument("-u", "--url", type=str, help="输入url地址", required=True)
    args = parser.parse_args()
    url = args.url
    ipv6_access_check(url)