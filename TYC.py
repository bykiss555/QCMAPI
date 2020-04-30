#-*- coding-8 -*-
import requests
import lxml
import sys
from bs4 import BeautifulSoup
import xlwt
import time
import urllib

def get_url(name):
    url = 'https://www.tianyancha.com/search?key='+name
    headers = {
            'Host': 'www.tianyancha.com',
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': r'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Referer': 'https://www.tianyancha.com/search?key=%E5%B1%B1%E4%B8%9C%20%E7%A7%91%E6%8A%80',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cookie': r'TYCID=588d3a007ad311ea95df9d0f0fcf432d; undefined=588d3a007ad311ea95df9d0f0fcf432d; ssuid=4563009864; _ga=GA1.2.1700354107.1586485872; tyc-user-phone=%255B%252218270882861%2522%255D; jsid=SEM-BAIDU-PZ2004-VI-000001; bad_id658cce70-d9dc-11e9-96c6-833900356dc6=94dba4a1-885d-11ea-96d6-c50fe8a2a16d; aliyungf_tc=AQAAANrkRUhjNg0A7tkiq8Lrzzhxigfc; csrfToken=zILzm1bnQ2vjYSnIeXVy53xX; bannerFlag=false; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1586485872,1586489456,1587974392,1588207098; _gid=GA1.2.2036986657.1588207098; token=7244f03947c54ddb82608831ba0ef9b8; _utm=aa707f12013f413caf276822fb86c45e; tyc-user-info=%257B%2522claimEditPoint%2522%253A%25220%2522%252C%2522vipToMonth%2522%253A%2522false%2522%252C%2522explainPoint%2522%253A%25220%2522%252C%2522integrity%2522%253A%252210%2525%2522%252C%2522state%2522%253A0%252C%2522announcementPoint%2522%253A%25220%2522%252C%2522bidSubscribe%2522%253A%2522-1%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522monitorUnreadCount%2522%253A%2522258%2522%252C%2522discussCommendCount%2522%253A%25220%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODI3MDg4Mjg2MSIsImlhdCI6MTU4ODIwNzEyMCwiZXhwIjoxNjE5NzQzMTIwfQ.EYLvVxx3Ofbnxol2jLhgJdfNgRagWSyZJrBrSKASfnA7gzyAZmlbyWq3UXCCBtREOOe8Gx9Wx7bvoXB-scNVbg%2522%252C%2522claimPoint%2522%253A%25220%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522myAnswerCount%2522%253A%25220%2522%252C%2522myQuestionCount%2522%253A%25220%2522%252C%2522signUp%2522%253A%25220%2522%252C%2522nickname%2522%253A%2522%25E5%2585%25B0%25E5%25A4%259A%25E8%258A%2599%25E6%2596%25AF%25E5%258D%25A1%2522%252C%2522privateMessagePointWeb%2522%253A%25220%2522%252C%2522privateMessagePoint%2522%253A%25220%2522%252C%2522isClaim%2522%253A%25220%2522%252C%2522pleaseAnswerCount%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522bizCardUnread%2522%253A%25220%2522%252C%2522mobile%2522%253A%252218270882861%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODI3MDg4Mjg2MSIsImlhdCI6MTU4ODIwNzEyMCwiZXhwIjoxNjE5NzQzMTIwfQ.EYLvVxx3Ofbnxol2jLhgJdfNgRagWSyZJrBrSKASfnA7gzyAZmlbyWq3UXCCBtREOOe8Gx9Wx7bvoXB-scNVbg; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1588208384',
            }

    response = requests.get(url,headers = headers)
    soup = BeautifulSoup(response.text,'lxml')
    com_all_info = soup.body.select('.mt74 .container.-top .container-left .search-block.header-block-container')[0]
    com_all_info_array = com_all_info.select('.search-item.sv-search-company')
    temp_g_url = com_all_info_array[0].select('.content .header .name')[0]['href']
    return temp_g_url

url = 'https://www.tianyancha.com/company/16327112'

headers = {
        'Host': 'www.tianyancha.com',
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': r'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Referer': 'https://www.tianyancha.com/search?key=%E5%B1%B1%E4%B8%9C%20%E7%A7%91%E6%8A%80',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cookie': r'TYCID=588d3a007ad311ea95df9d0f0fcf432d; undefined=588d3a007ad311ea95df9d0f0fcf432d; ssuid=4563009864; _ga=GA1.2.1700354107.1586485872; tyc-user-phone=%255B%252218270882861%2522%255D; jsid=SEM-BAIDU-PZ2004-VI-000001; bad_id658cce70-d9dc-11e9-96c6-833900356dc6=94dba4a1-885d-11ea-96d6-c50fe8a2a16d; aliyungf_tc=AQAAANrkRUhjNg0A7tkiq8Lrzzhxigfc; csrfToken=zILzm1bnQ2vjYSnIeXVy53xX; bannerFlag=false; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1586485872,1586489456,1587974392,1588207098; _gid=GA1.2.2036986657.1588207098; token=7244f03947c54ddb82608831ba0ef9b8; _utm=aa707f12013f413caf276822fb86c45e; tyc-user-info=%257B%2522claimEditPoint%2522%253A%25220%2522%252C%2522vipToMonth%2522%253A%2522false%2522%252C%2522explainPoint%2522%253A%25220%2522%252C%2522integrity%2522%253A%252210%2525%2522%252C%2522state%2522%253A0%252C%2522announcementPoint%2522%253A%25220%2522%252C%2522bidSubscribe%2522%253A%2522-1%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522monitorUnreadCount%2522%253A%2522258%2522%252C%2522discussCommendCount%2522%253A%25220%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODI3MDg4Mjg2MSIsImlhdCI6MTU4ODIwNzEyMCwiZXhwIjoxNjE5NzQzMTIwfQ.EYLvVxx3Ofbnxol2jLhgJdfNgRagWSyZJrBrSKASfnA7gzyAZmlbyWq3UXCCBtREOOe8Gx9Wx7bvoXB-scNVbg%2522%252C%2522claimPoint%2522%253A%25220%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522myAnswerCount%2522%253A%25220%2522%252C%2522myQuestionCount%2522%253A%25220%2522%252C%2522signUp%2522%253A%25220%2522%252C%2522nickname%2522%253A%2522%25E5%2585%25B0%25E5%25A4%259A%25E8%258A%2599%25E6%2596%25AF%25E5%258D%25A1%2522%252C%2522privateMessagePointWeb%2522%253A%25220%2522%252C%2522privateMessagePoint%2522%253A%25220%2522%252C%2522isClaim%2522%253A%25220%2522%252C%2522pleaseAnswerCount%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522bizCardUnread%2522%253A%25220%2522%252C%2522mobile%2522%253A%252218270882861%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODI3MDg4Mjg2MSIsImlhdCI6MTU4ODIwNzEyMCwiZXhwIjoxNjE5NzQzMTIwfQ.EYLvVxx3Ofbnxol2jLhgJdfNgRagWSyZJrBrSKASfnA7gzyAZmlbyWq3UXCCBtREOOe8Gx9Wx7bvoXB-scNVbg; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1588208384',
        }
html = requests.get(url,headers = headers)

soup = BeautifulSoup(html.text,'lxml')

com_all_info = soup.body.select('.mt74 .container.-top .company-warp.-public .tabline .tabline-right .container.company-header-block .box.-company-box')[0]
temp_g_name = com_all_info.select('.content .header .name')[0].text #获取公司名称
temp_g_phone = com_all_info.select('.content .detail .f0 .in-block.sup-ie-company-header-child-1')[0].find_all('span')[1].text #获取电话
temp_g_email = com_all_info.select('.content .detail .f0 .in-block.sup-ie-company-header-child-2 .email')[0].text #获取邮箱

print(temp_g_email)