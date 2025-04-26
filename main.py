from Crawling_support.Pen_Fun_Pavilion import Pen_Fun_Pavilion_main
import os


filename = '小说.txt'
def save_chapter(title, content, filename):
    with open(filename, 'a', encoding='UTF-8') as f:
        f.write(f"\n\n{title}\n\n")
        # 使用空格分割内容
        words = content.split()
        for word in words:
            f.write(word.strip() + '\n')


if __name__ == '__main__':
    url = input()

    if os.path.exists(filename):
        os.remove(filename)  # 如果文件已存在，先删除它
    Pen_Fun_Pavilion_main(url)
