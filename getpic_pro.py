#  #container > div > div > div:nth-child(3) > div.list_con_box > div.zt_con_img > dl > dd > ul > li:nth-child(21) > a > img

# 介绍 简单的图片下载，适用于简单的SRC超链接链接下载。适合初学者学习！
# 1. --**-- 引入包
import requests
from bs4 import BeautifulSoup

# 2. --**-- 模拟浏览器发送GET请求 得到了网站的页面信息
url = "https://www.tupianzj.com/"
main_resp = requests.get("https://www.tupianzj.com/meinv/mm/meizitu/")

# 状态码　：200 正常
# 302 ：重定向
# 404　：页面丢失
# 500　：服务器错误

main_resp.encoding = "gb2312"
# print(main_resp.text)

main_page = BeautifulSoup(main_resp.text, "html.parser")

a_lis = main_page.find("ul", class_="list_con_hot_ul").find_all("a")

# print(a_lis)  # 取到目标的图片链接地址第一级
n = 10
for a in a_lis:
    # child_url = a.find("a").get('href')
    child_url = a.get("href")
    # print(child_url)
    child_resp = requests.get(url + child_url)  # 获取网页内的信息
    child_resp.encoding = "gb2312"
    # print(child_resp.text)
    child_page = BeautifulSoup(child_resp.text, "html.parser")
    img_c = child_page.find("div", class_="pictu900")
    if img_c:  # 判断图片纯在
        img_b = child_page.find("div", class_="pictu900").find("img")
        print(img_b)
        # print(img_b.get("src"))
        # 下载图片
        img = img_b.get("src")
        with open(f"{n}.jpg", mode="wb") as f:
                f.write(requests.get(img).content)
                print("Download completed!")
    n += 1

# for a in a_lis:
#     child_url = a.get("href")  # 获取一级图片链接，get获取到分析的数据
#     child_resp = requests.get(child_url)  # 再一次获取到链接里的网页信息
#     child_resp.encoding = "utf-8"
#     child_page = BeautifulSoup(child_resp.text, "html.parser")
#     img_body = child_page.find("div", class_="ImageBody")
#     img = img_body.find("src")
#     if img: #  判断图片是否存在
#         jpg_src = img.get("src")
#         # 下载图片
#          with open(f"{n}.jpg", mode="wb") as f:
#              f.write(requests.get(jpg_src).content)
#          print("download comleted!")
#     n = n + 1
