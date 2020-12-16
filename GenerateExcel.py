import xlwt

# 1.创建 Workbook
wb = xlwt.Workbook()

# 2.创建 worksheet
ws = wb.add_sheet('sheet1')

# 3.写入第一行内容  ws.write(a, b, c)  a：行，b：列，c：内容
titleList = ['详情url', '标题', '楼盘名字', '面积大小']
for i in range(0, len(titleList)):
    ws.write(0, i, titleList[i])

# 4.写入对应内容
contentList = [{'title': '新村路地铁口 非顶楼边套全明 精装修 满五唯一', 'loupan': '2室1厅 | 55.82平米 | 南 | 精装 | 高楼层(共6层) | 1993年建 | 板楼',
                'houseType': '55.82平米', 'area': '南', 'toward': '精装', 'renovation': '高楼层(共6层)',
                'positionInfo': '双山小区-甘泉宜川', 'totalPrice': '285万', 'unitPrice': '单价51057元/平米',
                'detailUrl': 'https://sh.lianjia.com/ershoufang/107103371545.html'},
               {'title': '精装修南北两方 视野宽阔  近地铁 看房方便', 'loupan': '2室1厅 | 53.71平米 | 南 北 | 精装 | 高楼层(共6层) | 1988年建 | 板楼',
                'houseType': '53.71平米', 'area': '南 北', 'toward': '精装', 'renovation': '高楼层(共6层)',
                'positionInfo': '管弄一二街坊-光新', 'totalPrice': '295万', 'unitPrice': '单价54925元/平米',
                'detailUrl': 'https://sh.lianjia.com/ershoufang/107103058018.html'}
               ]

# 5.所需获取数据对应key
jsonKeyLIst = ['detailUrl', 'title', 'positionInfo', 'houseType']

for i in range(0, len(contentList)):
    for j in range(0, len(jsonKeyLIst)):
        # 文件中已写入一行title，所以这里写入内容时行号为i+1而非i
        # 列号为j
        ws.write(i + 1, j, contentList[i][jsonKeyLIst[j]])

# 保存文件
wb.save('./myExcel.csv')
wb.save('./myExcel.xls')
wb.save('./myExcel.xlsx')