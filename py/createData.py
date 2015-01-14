#coding:utf-8
import os
def constellation(birthday):
    rt = "unknown"
    if (len(birthday) == 8): 
        md = int(birthday[4:])
        if md >= 120 and md <= 219:
            rt = "Aquarius" #"水瓶座"
        elif md >= 220 and md <= 320:
            rt = "Pisces"#双鱼座"
        elif md >= 321 and md <= 420:
            rt = "Aries" #"白羊座"
	elif md >= 421 and md <= 521:
	    rt = "Taurus" #"金牛座"
	elif md >= 522 and md <= 621:
	    rt = "Gemini"#"双子座"
	elif md >= 622 and md <= 722:
	    rt = "Cancer"#"巨蟹座"
	elif md >= 723 and md <= 823:
	    rt = "Leo" #"狮子座"
	elif md >= 824 and md <= 923:
	    rt = "Virgo"#"处女座"
        elif md >= 924 and md <= 1023:
	    rt = "Libra"#"天秤座"
	elif md >= 1024 and md <= 1122:
	    rt = "Scorpio"#"天蝎座"
	elif md >= 1123 and md <= 1222:
	    rt =  "Sagittarius"#"射手座"
	elif (md >= 1223 and md <= 1231) or (md >= 101 and md <= 119):
	    rt = "Capricorn" # "摩蝎座"
	else:
	    rt = "unknown"
	
    return rt

f0 = open("/home/xunw/x/data/800W-1000W.csv")
def generateData(inDir,outPut):
   listfile=os.listdir(inDir) 
   print listfile
def readFile(filePath,outPut)
   fOut = open("/home/xunw/x/data/filter.csv",'w')
   head = f0.readline()
   print head
   print len(head.split(','))  #33
   i = 0 
   while i < 10:
       line = f0.readline()
       print line
       i += 1
       lineList =  line.split(',')
       if len(lineList) != 33:
           break
       strLine = lineList[0] +','+ lineList[4] +','+ lineList[5]+','+lineList[6]+','+constellation(lineList[6]) +'\n'
       fOut.write(strLine)
   print "write ok",i

