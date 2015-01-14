#coding:utf-8
def myfun(birthday):
    rt = "未知"
    if (len(birthday) == 8): 
        md = int(birthday[4:])
        if md >= 120 and md <= 219:
            rt = "水瓶座"
        elif md >= 220 and md <= 320:
            rt = "双鱼座"
        elif md >= 321 and md <= 420:
            rt = "白羊座"
	elif md >= 421 and md <= 521:
	    rt = "金牛座"
	elif md >= 522 and md <= 621:
	    rt = "双子座"
	elif md >= 622 and md <= 722:
	    rt = "巨蟹座"
	elif md >= 723 and md <= 823:
	    rt = "狮子座"
	elif md >= 824 and md <= 923:
	    rt = "处女座"
        elif md >= 924 and md <= 1023:
	    rt = "天秤座"
	elif md >= 1024 and md <= 1122:
	    rt = "天蝎座"
	elif md >= 1123 and md <= 1222:
	    rt = "射手座"
	elif (md >= 1223 and md <= 1231) or (md >= 101 and md <= 119):
	    rt = "摩蝎座"
	else:
	    rt = "未知"
	
    return rt
s = myfun("19901220")
print s
