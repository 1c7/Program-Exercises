# -*- coding: utf-8 -*-
from ConfigParser import ConfigParser
import os

cf = ConfigParser()
cf.read("aa.ini")
#初始化并读取配置文件


# s = cf.sections()
# print 'section:', s
# 获取所有sections,也就是配置文件中方括号抱起来的名字,如果是中文会被转换成其他编码

# o = cf.options("haha")
# print "haha options:", o
# 输出sections的所有key, 不包含值


# v = cf.items("haha")
# print v
# 获取指定sections下的所有key和value



# g = cf.get("haha","port")
# print g
# 获取指定sections下的指定key的值



# cf.set("haha","new","new-value")
# cf.write(open("aa.ini","w"))
# 给指定的sections下，设置新的key和value, 最后要写入才能保存


# cf.add_section("new section")
# cf.write(open("aa.ini","w"))
# 添加新的section.




# cf.remove_option("haha","url")
# cf.remove_section("test")
# cf.write(open("aa.ini","w"))

# 删除指定opertion,指定section
# 删除的section下的所有内容也会被删除











