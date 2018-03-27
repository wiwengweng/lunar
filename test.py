import lunar

JIEQI = lunar.JIE_QI_ADJUST_CALENDAR
jieqi = lunar.getJieqiList_byYear(2018,addNum=True)
# 输出2018年列表
for x in jieqi:
    print(JIEQI[x[1]],x[0])