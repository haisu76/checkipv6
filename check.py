import socket

def is_ipv6_supported(domain):
    try:
        # 使用getaddrinfo函数获取主机信息，如果返回IPv6地址，则表示支持IPv6
        socket.getaddrinfo(domain, None, socket.AF_INET6)
        return True
    except socket.gaierror:
        return False

# 要检测的目标网站
target_website = "example.com"  # 替换成你要测试的网站域名

if is_ipv6_supported(www.usst.edu.cn):
    print(f"{target_website} 支持IPv6")
else:
    print(f"{target_website} 不支持IPv6")
