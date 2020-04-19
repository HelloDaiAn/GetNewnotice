# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 15:48:10 2019
使用pdfminer来进行数据的处理，而不是pdfplumber,他可以进行一些数据的处理，还未完善
可以使用URopen来获得网页PDF内容并记性解析
@author: daian
"""
import requests
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBox
from pdfminer.pdfpage import PDFTextExtractionNotAllowed,PDFPage
from io import FileIO

HEADER = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}
url="http://static.cninfo.com.cn/finalpage/2019-04-29/1206134739.PDF"
r=requests.get(url,HEADER)
pdfFile=r.content
print(pdfFile)
f = open('temp.pdf', 'wb')
f.write(pdfFile)
f.close()
#pdfFile=urlopen("http://pythonscraping.com/pages/warandpeace/chapter1.pdf")

# 用文件对象来创建一个pdf文档分析器
praser = PDFParser(open('temp.pdf','rb'))
# 创建一个PDF文档
doc = PDFDocument(praser)
# 连接分析器 与文档对象
# 提供初始化密码
# 如果没有密码 就创建一个空的字符串
# 检测文档是否提供txt转换，不提供就忽略
if not doc.is_extractable:
    raise PDFTextExtractionNotAllowed
else:
    # 创建PDf 资源管理器 来管理共享资源
    rsrcmgr = PDFResourceManager()
    # 创建一个PDF设备对象
    laparams = LAParams()
    device = PDFPageAggregator(rsrcmgr, laparams=laparams)
    # 创建一个PDF解释器对象
    interpreter = PDFPageInterpreter(rsrcmgr, device)

    # 循环遍历列表，每次处理一个page的内容
    for page in PDFPage.create_pages(doc):
        interpreter.process_page(page)
        # 接受该页面的LTPage对象
        layout = device.get_result()
        # 这里layout是一个LTPage对象，里面存放着这个 page 解析出的各种对象
        # 包括 LTTextBox, LTFigure, LTImage, LTTextBoxHorizontal 等                            
        for x in layout:
            if isinstance(x, LTTextBox):
                print(x.get_text().strip())