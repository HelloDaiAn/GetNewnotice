# Financial-Notice
A python scripe that collecting financial data from ju-chao web, and can download pdf files from it , more important is it can parase data you want from pdf files using pdfplumber .
##usage 
START_DATE = '2019-10-16'
END_DATE = str(time.strftime('%Y-%m-%d'))
#盘中
intraday = False
#关键字
searchkey = '中国平安'
#股票代码
stock_code_set = ['']
#行业
industrys = ''
"industry": [
                {"key": "农、林、牧、渔业", "value": "农、林、牧、渔业"},
                {"key": "采矿业", "value": "采矿业"},
                {"key": "制造业", "value": "制造业"},
                {"key": "电力、热力、燃气及水生产和供应业", "value": "电力、热力、燃气及水生产和供应业"},
                {"key": "建筑业", "value": "建筑业"},
                {"key": "批发和零售业", "value": "批发和零售业"},
                {"key": "交通运输、仓储和邮政业", "value": "交通运输、仓储和邮政业"},
                {"key": "住宿和餐饮业", "value": "住宿和餐饮业"},
                {"key": "信息传输、软件和信息技术服务业", "value": "信息传输、软件和信息技术服务业"},
                {"key": "金融业", "value": "金融业"},
                {"key": "房地产业", "value": "房地产业"},
                {"key": "租赁和商务服务业", "value": "租赁和商务服务业"},
                {"key": "科学研究和技术服务业", "value": "科学研究和技术服务业"},
                {"key": "水利、环境和公共设施管理业", "value": "水利、环境和公共设施管理业"},
                {"key": "居民服务、修理和其他服务业", "value": "居民服务、修理和其他服务业"},
                {"key": "教育", "value": "教育"},
                {"key": "卫生和社会工作", "value": "卫生和社会工作"},
                {"key": "文化、体育和娱乐业", "value": "文化、体育和娱乐业"},
                {"key": "综合", "value": "综合"}
# 板块类型：szse: '深市' szseMain: '深主板',szseSme: '中小板',szseGem: '创业板',sse: '沪市',sseMain: '沪主板'，sseKcp: '科创板',hke: '港股',third: '三板',fund: '基金',bond: '债券',regulator: '监管',pre_disclosure: '预披露'，PLATE = 'shmb;
# 公告类型：
CATEGORY = ''
"category": [
                {"key": "category_ndbg_szsh", "value": "年报"},
                {"key": "category_bndbg_szsh", "value": "半年报"},
                {"key": "category_yjdbg_szsh", "value": "一季报"},
                {"key": "category_sjdbg_szsh", "value": "三季报"},
                {"key": "category_yjygjxz_szsh", "value": "业绩预告"},
                {"key": "category_qyfpxzcs_szsh", "value": "权益分派"},
                {"key": "category_dshgg_szsh", "value": "董事会"},
                {"key": "category_jshgg_szsh", "value": "监事会"},
                {"key": "category_gddh_szsh", "value": "股东大会"},
                {"key": "category_rcjy_szsh", "value": "日常经营"},
                {"key": "category_gszl_szsh", "value": "公司治理"},
                {"key": "category_zj_szsh", "value": "中介报告"},
                {"key": "category_sf_szsh", "value": "首发"},
                {"key": "category_zf_szsh", "value": "增发"},
                {"key": "category_gqjl_szsh", "value": "股权激励"},
                {"key": "category_pg_szsh", "value": "配股"},
                {"key": "category_jj_szsh", "value": "解禁"},
                {"key": "category_gszq_szsh", "value": "公司债"},
                {"key": "category_kzzq_szsh", "value": "可转债"},
                {"key": "category_qtrz_szsh", "value": "其他融资"},
                {"key": "category_gqbd_szsh", "value": "股权变动"},
                {"key": "category_bcgz_szsh", "value": "补充更正"},
                {"key": "category_cqdq_szsh", "value": "澄清致歉"},
                {"key": "category_fxts_szsh", "value": "风险提示"},
                {"key": "category_tbclts_szsh", "value": "特别处理和退市"},
                {"key": "category_tszlq_szsh", "value": "退市整理期"}
### platform:  
### win10 anaconda python3.7 
['601318中国平安2019年年度股东大会决议公告.(334k).PDF', 'http://static.cninfo.com.cn/finalpage/2020-04-10/1207473251.PDF']
['601318中国平安2019年年度股东大会法律意见书.(399k).PDF', 'http://static.cninfo.com.cn/finalpage/2020-04-10/1207473250.PDF']
['601318中国平安关于疫情防控期间参加2019年年度股东大会相关注意事项的第三次提示性公告.(380k).PDF', 'http://static.cninfo.com.cn/finalpage/2020-04-07/1207458303.PDF']
['601318中国平安关于疫情防控期间参加2019年年度股东大会相关注意事项的第二次提示性公告.(380k).PDF', 'http://static.cninfo.com.cn/finalpage/2020-03-28/1207419364.PDF']
['601318中国平安关于疫情防控期间参加2019年年度股东大会相关注意事项的提示性公告.(379k).PDF', 'http://static.cninfo.com.cn/finalpage/2020-03-21/1207390672.PDF']
['601318中国平安关于2019年年度股东大会增加临时提案的公告.(463k).PDF', 'http://static.cninfo.com.cn/finalpage/2020-03-19/1207383752.PDF']
['601318中国平安2019年年度股东大会资料.(619k).PDF', 'http://static.cninfo.com.cn/finalpage/2020-03-19/1207383751.PDF']
['601318中国平安关于2020年度核心人员持股计划完成股票购买的公告.(149k).PDF', 'http://static.cninfo.com.cn/finalpage/2020-03-02/1207336364.PDF']
['601318中国平安关于2020年度长期服务计划完成股票购买的公告.(151k).PDF', 'http://static.cninfo.com.cn/finalpage/2020-03-02/1207336363.PDF']
['601318中国平安关于召开2019年年度股东大会的通知.(505k).PDF', 'http://static.cninfo.com.cn/finalpage/2020-02-22/1207317877.PDF']
['601318中国平安普华永道中天会计师事务所(特殊普通合伙)关于中国平安保险(集团)股份有限公司2019年度会计估计变更的专项报告.(596k).PDF', 'http://static.cninfo.com.cn/finalpage/2020-02-21/1207316211.PDF']
['601318中国平安董事会审计与风险管理委员会2019年度履职情况报告.(163k).PDF', 'http://static.cninfo.com.cn/finalpage/2020-02-21/1207316209.PDF']
['601318中国平安2019年年度投资者保护工作报告.(162k).PDF', 'http://static.cninfo.com.cn/finalpage/2020-02-21/1207316206.PDF']
['601318中国平安2019年年度报告.(8670k).PDF', 'http://static.cninfo.com.cn/finalpage/2020-02-21/1207316204.PDF']
['601318中国平安2019年年度利润分配方案公告.(415k).PDF', 'http://static.cninfo.com.cn/finalpage/2020-02-21/1207316202.PDF']
['601318中国平安2019年度已审财务报表.(5710k).PDF', 'http://static.cninfo.com.cn/finalpage/2020-02-21/1207316197.PDF']
['601318中国平安2019年度独立董事述职报告.(279k).PDF', 'http://static.cninfo.com.cn/finalpage/2020-02-21/1207316195.PDF']
['601318中国平安2019年度内部控制评价报告.(630k).PDF', 'http://static.cninfo.com.cn/finalpage/2020-02-21/1207316194.PDF']
['600315上海家化关于2020年度与中国平安保险(集团)股份有限公司及其附属企业日常关联交易公告.(219k).PDF', 'http://static.cninfo.com.cn/finalpage/2020-02-20/1207314454.PDF']
['601318中国平安关于征集2019年度业绩发布会问题的公告.(137k).PDF', 'http://static.cninfo.com.cn/finalpage/2020-02-15/1207307153.PDF']
['601318中国平安平安银行股份有限公司2019年度业绩快报公告.(103k).PDF', 'http://static.cninfo.com.cn/finalpage/2020-01-14/1207246487.PDF']
['601318中国平安关于披露平安银行2019年度业绩快报的公告.(177k).PDF', 'http://static.cninfo.com.cn/finalpage/2020-01-14/1207246486.PDF']
********time to open processing all files are 6.152313470840454*********

Process finished with exit code 0
