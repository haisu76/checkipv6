import requests
import sys
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def get_all_sub_links(base_url):
    visited_links = set()
    to_visit = [base_url]

    while to_visit:
        current_url = to_visit.pop()
        if current_url in visited_links:
            continue

        try:
            response = requests.get(current_url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                visited_links.add(current_url)

                for link in soup.find_all('a', href=True):
                    absolute_link = urljoin(current_url, link['href'])
                    if base_url in absolute_link and absolute_link not in visited_links:
                        to_visit.append(absolute_link)
        except Exception as e:
            print(f"Error accessing {current_url}: {str(e)}")

    return visited_links

if __name__ == "__main__":
    
    # if len(sys.argv) != 2:
        # print("请提供一个检测网站地址。")
        # return

    # 获取参数值
    input_parameter = sys.argv[1]

    # 在代码中使用参数值
    # print(f"你提供的网址是：{input_parameter}")


    target_url = "input_parameter"  # 替换成你的目标网站


    all_sub_links = get_all_sub_links(target_url)

    for link in all_sub_links:
        print(link)


# 打开一个文件以进行写入（如果文件不存在将创建一个新文件）
file_path = "2-links.txt"  # 文件路径，可以根据需要自定义

# 使用 "w" 模式打开文件，表示写入模式
with open(file_path, "w") as file:
    # 将要保存到文件的内容写入文件
    for item in all_sub_links:
        file.write(item + "\n")


# 文件会在退出 "with" 代码块后自动关闭
print("链接地址已成功保存到文件。")
