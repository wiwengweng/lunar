import lunar

JIEQI = lunar.JIE_QI
jieqi = lunar.getJieqiList_byMonth(2018,5,addNum=True)
# 小寒和大寒总在一月份
print(jieqi)