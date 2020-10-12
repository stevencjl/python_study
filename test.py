# --**-- 爬取豆瓣排行前250的电影名称
# --**-- 主用库 requests 和 BeautifulSoup


import requests
from bs4 import BeautifulSoup


class Douban:

    def __init__(self):
        self.URL = 'https://movie.douban.com/top250'
        self.startnum = []
        for star_num in range(0, 251, 25):
            self.startnum.append(star_num)
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}

    def get_top250(self):
        for start in self.startnum:
            start = str(start)
            html = requests.get(self.URL, params={'start': start}, headers=self.header)
            soup = BeautifulSoup(html.text, 'html.parser')
            name = soup.select(
                '#content > div > div.article > ol > li > div > div.info > div.hd > a > span:nth-child(1)')
            for name in name:
                print(name.get_text())
