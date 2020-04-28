import requests
from bs4 import BeautifulSoup
import re
import time
import sys
import urllib.request
import xlwt
from lxml import etree
import json
from multiprocessing import Pool
import xlrd
def read_excel(): #读取xls文件数据
    path = str(input('请输入需要提取文件的路径：'))
    sure = str(input('行 or 列：'))
    #print(path) #确认路径是否正确
    number = int(input('需要提取的数值；'))
    workbook = xlrd.open_workbook(path)
    sheet_name = workbook.sheet_names()[0]
    # 根据sheet索引或者名称获取sheet内容
    sheet = workbook.sheet_by_index(0)  # sheet索引从0开始
    # 获取整行和整列的值（数组）
    rows = sheet.row_values(number)  # 获取第1行内容
    cols = sheet.col_values(number)  # 获取第0列内容
    if sure == '行' :
        return rows
    else:
        return cols

def getHtmlText(url,header): #Get网页源代码
    try:
        html = requests.get(url,headers=header)
        html.raise_for_status()
        html.encoding = html.apparent_encoding
        #print(html.raise_for_status())
        #print(html.text)
        return html.text
    except:
        print('访问失败')
def getListinfo(html): #从交易网获取企业名称
    jsonData = json.loads(html)
    getData = jsonData.get('return')
    data = json.loads(getData)
    Listinfo = []
    i = 0
    getTable = data.get('Table')
    for List in getTable:
        qymcList = getTable[i].get('qymc')
        Listinfo.append(qymcList)
        i += 1
    return Listinfo
def getUrl(page): #交易网请求网址合成
    url = ''
    onepage = str(page)
    headUrl = 'http://www.jxsggzy.cn/jxggzy/services/JyxxWebservice/getTradeList?response=application/json&pageIndex='
    footUrl = '&pageSize=22&&dsname=ztb_data&bname=&qytype=3&itemvalue=131'
    url = headUrl + onepage + footUrl
    return url
def allqymcList(): #确认需要请求的页数
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36',
        'referer': 'http://www.jxsggzy.cn/web/tradeSubject_list.html',
        'Cookie': 'JSESSIONID=6E8A83AF7E01C129FF5B91317771B3AC; _CSRFCOOKIE=C040DA20A104FA8DA84ECB1C1B687FAFEDABC045',
        'Host': 'www.jxsggzy.cn'}
    allList = []
    starPage = input(" 请输入开始页码(1-323)：")
    endPage = int(input(" 请输入结束页码(1-323)："))
    page = int(starPage)
    while (page <= endPage):
        allList += getListinfo(getHtmlText(getUrl(page), header))
        page += 1
    print('共计', len(allList), '条')
    return allList

def getToken(): #企查猫获取Token
    url = 'http://api.qianzhan.com/OpenPlatformService/GetToken?type=JSON&appkey=189215e8d865c97b&seckey=b4e5c3bd9abebad4'
    searchToken = requests.get(url).text
    jsonData = json.loads(searchToken)
    resultToken = jsonData.get('result')
    Token = resultToken['token']
    return Token
def getMassage(url): #从企查猫接口获取数据
    getMassage = []
    html = requests.get(url).content
    # print(html)
    soup = BeautifulSoup(html, 'lxml')
    jsonData = soup.find('p').get_text()
    print(jsonData)
    #status = jsonData.loads(jsonData).get('status')
    try:
        resultData = json.loads(jsonData).get('result')
        #resultData = json.loads(Data)
        print(resultData)
        #print(type(resultData))
        companyName = resultData.get('companyName') #公司名称
        #companyType = resultData.get('companyType') #公司类型
        faRen = resultData.get('faRen') #公司法人
        address = resultData.get('address') #公司地址
        phone = resultData.get('phone') #公司电话
        email = resultData.get('email') #邮件
        getMassage.append(companyName)
        getMassage.append(faRen)
        getMassage.append(phone)
        getMassage.append(address)
        getMassage.append(email)
    except:
        companyName = '空'  # 公司名称
        # companyType = resultData.get('companyType') #公司类型
        faRen = '空'  # 公司法人
        address = '空'  # 公司地址
        phone = '空'  # 公司电话
        email = '空'  # 邮件
        getMassage.append(companyName)
        getMassage.append(faRen)
        getMassage.append(phone)
        getMassage.append(address)
        getMassage.append(email)
        print('查找不到该公司')
    return getMassage

def searchCompany(Cname): #企业查询
    rname = urllib.parse.quote(Cname)
    headUrl = '	http://api.qianzhan.com/OpenPlatformService/OrgCompanyListByCompanyName?token='
    token = getToken()
    footUrl = '&companyName='+rname
    Url = headUrl+token+footUrl
    Massage = getMassage(Url)
    return Massage
def main():
    global allqymc
    allqymc = read_excel()
    print(len(allqymc))
    i = 0
    m = 0
    workbook = xlwt.Workbook()
    sheet1 = workbook.add_sheet('sheet1', cell_overwrite_ok=True)
    name_list = ['公司名字', '法定代表人', '联系方式', '公司地址', '公司邮件']
    for cc in range(0, len(name_list)):
        sheet1.write(0, cc, name_list[cc])
    try:
        for m in allqymc:
            allList = searchCompany(m)
            sheet1.write(i + 1, 0, allList[0])  # 公司名字
            sheet1.write(i + 1, 1, allList[1])  # 法定代表人
            sheet1.write(i + 1, 2, allList[2])  # 联系方式
            sheet1.write(i + 1, 3, allList[3])  # 公司地址
            sheet1.write(i + 1, 4, allList[4])  # 邮件地址
            i+=1
        workbook.save('E:\\省外.xls')
        print('全部查询完毕，数据已保存')
    except:
        workbook.save('E:\\省外.xls')
        print('查询出错，以保存部分数据')

    print('数据已保存')


if __name__=='__main__':
    main()









