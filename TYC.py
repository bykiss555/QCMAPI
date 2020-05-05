#-*- coding-8 -*-
import requests
import lxml
import sys
from bs4 import BeautifulSoup
import xlwt
import xlrd
import time
import urllib
import os

def get_url(name,headers):
    url = 'https://www.tianyancha.com/search?key='+name
    response = requests.get(url,headers = headers)
    soup = BeautifulSoup(response.text,'lxml')
    com_all_info = soup.body.select('.mt74 .container.-top .container-left .search-block.header-block-container')[0]
    com_all_info_array = com_all_info.select('.search-item.sv-search-company')
    temp_g_url = com_all_info_array[0].select('.content .header .name')[0]['href']
    return temp_g_url


def get_informations(url,headers):
    print('我没有问题')
    get_information = []

    html = requests.get(url,headers = headers)
    html.raise_for_status()
    html.encoding = html.apparent_encoding
    print(html.raise_for_status())
    print('我没有问题1')

    soup = BeautifulSoup(html.text,'lxml')
    print('我没有问题2')
    com_all_info = soup.body.select('.mt74 .container.-top .company-warp.-public .tabline .tabline-right .container.company-header-block .box.-company-box')[0]
    temp_g_name = com_all_info.select('.content .header .name')[0].text #获取公司名称
    temp_g_phone = com_all_info.select('.content .detail .f0 .in-block.sup-ie-company-header-child-1')[0].find_all('span')[1].text #获取电话
    temp_g_email = com_all_info.select('.content .detail .f0 .in-block.sup-ie-company-header-child-2 .email')[0].text #获取邮箱
    temp_g_url = com_all_info.select('.content .detail .f0.clearfix .in-block.sup-ie-company-header-child-1')[0].text.strip('网址：') #获取官网
    temp_g_adress = com_all_info.select('.content .detail .f0.clearfix .in-block.sup-ie-company-header-child-2 .auto-folder')[0].find_all('div')[0].text #获取地址
    print('我没有问题3')
    com_all_table = soup.body.select('.mt74 .container.-top .company-warp.-public .container .container-left.tabline .box-container.-main .detail-list .block-data-group .block-data .data-content')[0]
    temp_g_faren = com_all_table.select('.table .name')[0].text #获取法人
    com_all_table_2 = com_all_table.select('.table.-striped-col.-border-top-none.-breakall')[0].find_all('td') #获取企业信息
    temp_g_money = com_all_table_2[1].text #获取资本
    temp_g_regtime = com_all_table_2[6].text #获取成立时间
    temp_g_tatus = com_all_table_2[8].text #获取公司状态
    temp_g_creditcode = com_all_table_2[10].text #获取统一社会信用代码
    temp_g_type = com_all_table_2[18].text #获取公司类型
    temp_g_industry = com_all_table_2[20].text #获取公司行业
    temp_g_scope = com_all_table_2[40].text #获取公司经营范围
    print('我没有问题4')
    get_information.append(temp_g_name)
    get_information.append(temp_g_creditcode)
    get_information.append(temp_g_faren)
    get_information.append(temp_g_type)
    get_information.append(temp_g_industry)
    get_information.append(temp_g_regtime)
    get_information.append(temp_g_money)
    get_information.append(temp_g_adress)
    get_information.append(temp_g_email)
    get_information.append(temp_g_phone)
    get_information.append(temp_g_url)
    #get_information.append(temp_g_tatus)
    get_information.append(temp_g_scope)
    return  get_information
def main():
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
        'Cookie': r'TYCID=7c9d10708b8911ea983e3f3e94033f7c; undefined=7c9d10708b8911ea983e3f3e94033f7c; ssuid=2526084114; _ga=GA1.2.199054581.1588323332; jsid=SEM-BAIDU-PZ2005-SY-000001; tyc-user-info=%257B%2522claimEditPoint%2522%253A%25220%2522%252C%2522vipToMonth%2522%253A%2522false%2522%252C%2522explainPoint%2522%253A%25220%2522%252C%2522integrity%2522%253A%252210%2525%2522%252C%2522state%2522%253A%25220%2522%252C%2522announcementPoint%2522%253A%25220%2522%252C%2522bidSubscribe%2522%253A%2522-1%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522monitorUnreadCount%2522%253A%2522260%2522%252C%2522discussCommendCount%2522%253A%25220%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODI3MDg4Mjg2MSIsImlhdCI6MTU4ODM0MDM1NiwiZXhwIjoxNjE5ODc2MzU2fQ.O6M16LLI-FKMUZSC7UEk2X1zO9MxcggQOshMEgQMtevXihx6eSmSXcb6_CJLSUA-JTsVG_gXLdDwWN90hZQpdg%2522%252C%2522claimPoint%2522%253A%25220%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522myAnswerCount%2522%253A%25220%2522%252C%2522myQuestionCount%2522%253A%25220%2522%252C%2522signUp%2522%253A%25220%2522%252C%2522nickname%2522%253A%2522%25E5%2585%25B0%25E5%25A4%259A%25E8%258A%2599%25E6%2596%25AF%25E5%258D%25A1%2522%252C%2522privateMessagePointWeb%2522%253A%25220%2522%252C%2522privateMessagePoint%2522%253A%25220%2522%252C%2522isClaim%2522%253A%25220%2522%252C%2522pleaseAnswerCount%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522bizCardUnread%2522%253A%25220%2522%252C%2522mobile%2522%253A%252218270882861%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODI3MDg4Mjg2MSIsImlhdCI6MTU4ODM0MDM1NiwiZXhwIjoxNjE5ODc2MzU2fQ.O6M16LLI-FKMUZSC7UEk2X1zO9MxcggQOshMEgQMtevXihx6eSmSXcb6_CJLSUA-JTsVG_gXLdDwWN90hZQpdg; tyc-user-phone=%255B%252218270882861%2522%255D; aliyungf_tc=AQAAAOpTkm5HJQUAcs9vtnE2YWQSVmaz; csrfToken=KqstB0aXGIZZV3740-eHW2WU; bannerFlag=false; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1588323331,1588325334,1588595095; _gid=GA1.2.1829183203.1588595096; _gat_gtag_UA_123487620_1=1; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1588595103; RTYCID=7b32afbfe3994280acd8c49e272c051c; token=39caafded045409298df421ef766b3ce; _utm=99ff34f0d6ad47e996eebbc729528d0a; CT_TYCID=22754c7f89b44657a951c168b8badc2c; cloud_token=cdca7d0248df48489e8af3548990cafb; cloud_utm=381ecdc3c5894372bf080b4a8050c741',
    }
    k=0
    i=1
    myfile = xlrd.open_workbook(r'G:\Python\QCMAPI\cxwj.xlsx')
    #sheets = myfile.sheet_names()#读取sheet名
    first_table = myfile.sheet_by_index(2)
    first_col = first_table.col_values(0)
    num =len(first_col) #查询个数
    print('需要查询的数量为：',num)
    workbook=xlwt.Workbook()
    sheet1 = workbook.add_sheet('sheet1',cell_overwrite_ok=True)
    sheet1.write(0,0,'企业名称')
    sheet1.write(0,2,'统一社会信用代码')
    sheet1.write(0,3,'法定代表人')
    sheet1.write(0,4,'企业类型')
    sheet1.write(0,5,'企业行业')
    sheet1.write(0,6,'成立日期')
    sheet1.write(0,7,'注册资本')
    sheet1.write(0,8,'地址')
    sheet1.write(0,9,'邮箱')
    sheet1.write(0,10,'电话号码')
    sheet1.write(0,11,'网址')
    #sheet1.write(0,12,'企业状态')
    sheet1.write(0,12,'经营范围')
    # try:
    #
    #     while (k<num):
    #
    #         url = get_url(first_col[k],headers)
    #         print('正在查询：',first_col[k])
    #         print('查询地址为：',url)
    #         result = get_informations(url,headers)
    #         sheet1.write(i,0,result[0])
    #         sheet1.write(i,1,result[1])
    #         sheet1.write(i,2,result[2])
    #         sheet1.write(i,3,result[3])
    #         sheet1.write(i,4,result[4])
    #         sheet1.write(i,5,result[5])
    #         sheet1.write(i,6,result[6])
    #         sheet1.write(i,7,result[7])
    #         sheet1.write(i,8,result[8])
    #         sheet1.write(i,9,result[9])
    #         sheet1.write(i,10,result[10])
    #         sheet1.write(i,11,result[11])
    #         sheet1.write(i,12,result[12])
    #         sheet1.write(i,13,result[13])
    #         time.sleep(10)
    #         i=i+1
    #         k=k+1
    #
    #     name = str(input('请输入保存文件名：'))
    #     path = os.getcwd() + '\\'
    #     print('你保存文件的位置：', path + name + '.xls')
    #     print('任务已结束')
    # except:
    #     print('出错啦！！！已查询到：',first_col[k],' 请及时保存')
    #     name = str(input('请输入保存文件名：'))
    #     path = os.getcwd() + '\\'
    #     workbook.save(path + name + '.xls')
    #     print('你保存文件的位置：',path + name +'.xls')
    #     print('任务已结束')
    while (k<num):

        url = get_url(first_col[k],headers)
        print('正在查询：',first_col[k])
        print('查询地址为：',url)
        result = get_informations(url,headers)
        sheet1.write(i,0,result[0])
        sheet1.write(i,1,result[1])
        sheet1.write(i,2,result[2])
        sheet1.write(i,3,result[3])
        sheet1.write(i,4,result[4])
        sheet1.write(i,5,result[5])
        sheet1.write(i,6,result[6])
        sheet1.write(i,7,result[7])
        sheet1.write(i,8,result[8])
        sheet1.write(i,9,result[9])
        sheet1.write(i,10,result[10])
        sheet1.write(i,11,result[11])
        #sheet1.write(i,12,result[12])
        #sheet1.write(i,13,result[13])
        time.sleep(10)
        i=i+1
        k=k+1

    name = str(input('请输入保存文件名：'))
    path = os.getcwd() + '\\'
    print('你保存文件的位置：', path + name + '.xls')
    print('任务已结束')

if __name__=='__main__':
    main()





