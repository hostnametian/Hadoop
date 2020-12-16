# -*- coding: UTF-8 -*-
import sys
import re

# 设置key
key = "k"
for line in sys.stdin:
    # 去掉前面的url地址了
    line = re.split("\t", line)[1]
    # 替换特殊字符
    line = line.replace(" —", "")
    # 替换一些标点符号
    line = re.sub("[,.;()«»-]", "", line)
    # 按空格分隔
    words = re.split(r"\s", line)

    # 循环
    for word in words:
        # 过滤为空的
        if word != '':
            print ("%s\t%s|%d" % (key, word, len(word)))



