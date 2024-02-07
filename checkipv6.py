import argparse
import socket

def is_ipv6_supported(domain):
    try:
        # 使用 getaddrinfo 函数获取主机信息，如果返回 IPv6 地址，则表示支持 IPv6
        socket.getaddrinfo(domain, None, socket.AF_INET6)
        return True
    except socket.gaierror:
        return False

def main():
    parser = argparse.ArgumentParser(description="检测网站是否支持IPv6")
    parser.add_argument("website", help="要检测的网站域名")
    args = parser.parse_args()

    website = args.website

    if is_ipv6_supported(website):
        print(f"{website} 支持IPv6")
    else:
        print(f"{website} 不支持IPv6")

if __name__ == "__main__":
    main()
