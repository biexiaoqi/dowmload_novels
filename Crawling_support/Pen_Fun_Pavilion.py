import requests
from bs4 import BeautifulSoup
import time

from main import save_chapter, filename


def get_Pen_Fun_Pavilion(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/130.0.0.0 Safari/537.36'
    }
    try:
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, 'html.parser')
        content = soup.find_all('div')[4].text
        title = soup.find('span').text
        next_chapter = soup.find_all('a')[9].get('href')
        return title, content, next_chapter
    except requests.RequestException as e:
        print(f"获取章节内容时发生错误: {e}")
        return None, None, None





def Pen_Fun_Pavilion_main(start_url):
    base_url = 'https://a4f554eb2c093.bi48.cc'

    url = start_url
    chapter_count = 0

    while True:
        title, content, next_chapter = get_Pen_Fun_Pavilion(url)

        if title is None:  # 如果获取内容失败，尝试重新获取
            print("获取章节失败，5秒后重试...")
            time.sleep(5)
            continue

        save_chapter(title, content, filename)
        chapter_count += 1
        print(f"已保存第 {chapter_count} 章: {title}")

        if not next_chapter:
            print("小说爬取完成！")
            break

        url = base_url + next_chapter
        time.sleep(1)  # 添加延迟，避免请求过于频繁
