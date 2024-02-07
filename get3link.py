import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def get_all_links(base_url, max_depth=3, current_depth=1):
    if current_depth > max_depth:
        return []

    visited_links = set()
    to_visit = [base_url]
    all_links = []

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
                        all_links.append(absolute_link)
        except Exception as e:
            print(f"Error accessing {current_url}: {str(e)}")

    return all_links

if __name__ == "__main__":
    target_url = "https://www.usst.edu.cn"  # 替换成你的目标网站
    all_third_level_links = get_all_links(target_url, max_depth=3)

    for link in all_third_level_links:
        print(link)
