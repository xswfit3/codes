#coding:utf-8
import os
from pyspark import SparkContext
from pyspark.sql import SQLContext
from pyspark.sql import Row, StructField, StructType, StringType, IntegerType

def myfun(birthday):
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



if __name__ == "__main__":
    sc = SparkContext(appName="PythonSQL")
    sqlContext = SQLContext(sc)

    # RDD is created from a list of rows
    lines = sc.textFile("/home/xunw/x/data/filter.csv")
    parts = lines.map(lambda l: l.split(","))
    people = parts.map(lambda p: Row(name=p[0], card=p[1],sex=p[2],birthday=p[3]))

# Infer the schema, and register the SchemaRDD as a table.
    schemaPeople = sqlContext.inferSchema(people)
    schemaPeople.registerTempTable("users")
    sqlContext.registerFunction("constellation", lambda x :myfun(x))
    result = sqlContext.sql("SELECT constellation(birthday), count(constellation(birthday)) FROM users group by constellation(birthday)")
    ans = result.collect()
    for a in ans:
        print a[0]+ ": " + str(a[1]) 
