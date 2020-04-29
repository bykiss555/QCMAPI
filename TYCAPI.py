import requests
from bs4 import BeautifulSoup
import lxml
from lxml import etree
import xlwt
import xlrd
import json
import jsonpath
import os
global token
def gerResult(k,first_col)
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3756.400 QQBrowser/10.5.4039.400','Authorization':'9b8d85f5-5c15-44f0-bc43-2856fb93a7a6'}
    url  = 'https://open.api.tianyancha.com/services/open/ic/baseinfoV2/2.0?id=&name='+first_col[k]
    html = requests.get(url,headers=headers)
    jsondata = json.loads(html)
	result = jsondata.get('result')
	return result
    
html = '''
{
  "result": {
    "regStatus": "存续",
    "regCapital": "567万人民币",
    "industry": "研究和试验发展",
    "type": 1,
    "legalPersonName": "石玲娟",
    "regNumber": "360100110011316",
    "property3": "Nanchang Construction Technology Consulting Supervision Co.,Ltd.",
    "creditCode": "91360100158382213N",
    "fromTime": 708192000000,
    "approvedTime": 1524672000000,
    "alias": "建筑",
    "companyOrgType": "其他有限责任公司",
    "id": 460328737,
    "orgNumber": "158382213",
    "toTime": 2664633600000,
    "email": "573021027@qq.com",
    "actualCapital": "566.999万人民币",
    "estiblishTime": 708192000000,
    "regInstitute": "南昌市市场和质量监督管理局",
    "taxNumber": "91360100158382213N",
    "businessScope": "工程建设监理、标底测算、招投标代理、建设技术咨询、工程项目评估、工程项目管理、工程技术咨询及造价咨询、工程预算、审计、工程担保、工程质量监督、检查、其他工程管理服务、建筑技术培训、技术服务、技术转让、可行性研究、组织建筑技术交流(以上项目依法需经批准的项目，需经相关部门批准后方可开展经营活动)",
    "regLocation": "江西省南昌市东湖区富大有路9号赣昌大厦11楼（1101-1103室和1108-1112室）",
    "websiteList": "www.ncjzjl.cn",
    "phoneNumber": "0791-86595324",
    "name": "南昌市建筑技术咨询监理有限公司",
    "percentileScore": 6751,
    "industryAll": {
      "categoryMiddle": "  社会人文科学研究",
      "categoryBig": "研究和试验发展",
      "category": "科学研究和技术服务业",
      "categorySmall": ""
    },
    "isMicroEnt": 0,
    "base": "jx"
  },
  "reason": "ok",
  "error_code": 0
}
'''

# 			result = getResult(getHtml(k,token,first_col))
# 			sheet1.write(i,0,result['name'])
# 			sheet1.write(i,3,result['creditCode'])
# 			sheet1.write(i,4,result['legalPersonNam'])
# 			sheet1.write(i,5,result['companyOrgType'])
# 			sheet1.write(i,7,result['actualCapital'])
# 			sheet1.write(i,8,result['regLocation'])
# 			sheet1.write(i,9,result['email'])
# 			sheet1.write(i,10,result['businessScope'])
# 			sheet1.write(i,11,result['phoneNumber'])
# 			sheet1.write(i,12,result['websiteList'])

#获取请求连接
# def getHtml(k,token,first_col):
#     headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3756.400 QQBrowser/10.5.4039.400','Authorization':'9b8d85f5-5c15-44f0-bc43-2856fb93a7a6'}
# 	head  = 'https://open.tianyancha.com/cloud-open-api/services/open/ic/baseinfoV2/2.0.json?id=&name='
# 	url = head + token + '&type=JSON&companyName=' + first_col[k]
# 	html = requests.get(url)
# 	print('正在查询：',first_col[k])
# 	return html.text

#获取字典信息
def getResult(html):
	jsondata = json.loads(html)
	result = jsondata.get('result')
	return result


# def main():
# 	k = 0
# 	i = 1
# 	token = getToken()
# 	print(token)
# 	myfile = xlrd.open_workbook(r'D:\Python\cxwj.xlsx')
# 	#sheets = myfile.sheet_names()#读取sheet名
# 	first_table = myfile.sheet_by_index(2)
# 	first_col = first_table.col_values(0)
# 	num =len(first_col) #查询个数
# 	print('需要查询的数量为：',num)
# 	workbook=xlwt.Workbook()
# 	sheet1=workbook.add_sheet('sheet1',cell_overwrite_ok=True)
# 	sheet1.write(0,0,'企业名称')
# 	sheet1.write(0,1,'省份')
# 	sheet1.write(0,2,'城市')
# 	sheet1.write(0,3,'统一社会信用代码')
# 	sheet1.write(0,4,'法定代表人')
# 	sheet1.write(0,5,'企业类型')
# 	sheet1.write(0,6,'成立日期')
# 	sheet1.write(0,7,'注册资本')
# 	sheet1.write(0,8,'地址')
# 	sheet1.write(0,9,'邮箱')
# 	sheet1.write(0,10,'经营范围')
# 	sheet1.write(0,11,'网址')
# 	sheet1.write(0,12,'电话号码')
# 	try:
# 		while (k<num):

# 			result = getResult(getHtml(k,token,first_col))
# 			sheet1.write(i,0,result['companyName'])
# 			sheet1.write(i,1,result['provinceName'])
# 			sheet1.write(i,2,result['areaName'])
# 			sheet1.write(i,3,result['creditCode'])
# 			sheet1.write(i,4,result['faRen'])
# 			sheet1.write(i,5,result['regType'])
# 			sheet1.write(i,6,result['issueTime'])
# 			sheet1.write(i,7,result['regMoney'])
# 			sheet1.write(i,8,result['address'])
# 			sheet1.write(i,9,result['email'])
# 			sheet1.write(i,10,result['bussinessDes'])
# 			sheet1.write(i,11,result['phone'])
# 			sheet1.write(i,12,result['webSite'])
# 			i=i+1
# 			k=k+1
# 		name = str(input('请输入保存文件名：'))
# 		path = os.getcwd() + '\\'
# 		workbook.save(path + name + '.xls')
# 		print('你保存文件的位置：',path + name +'.xls')
# 		print('任务已结束')
# 	except:
# 		name = str(input('请输入保存文件名：'))
# 		path = os.getcwd() + '\\'
# 		workbook.save(path + name + '.xls')
# 		print('你保存文件的位置：',path + name +'.xls')
# 		print('任务已结束')


# if __name__=='__main__':
#     main()