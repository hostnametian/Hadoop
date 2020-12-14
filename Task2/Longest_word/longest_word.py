# -*- coding: UTF-8 -*-

from mrjob.job import MRJob
from mrjob.protocol import TextProtocol
import re
"""
Напишите программу, чтобы найти самое длинное слово.
"""


class langgest_word(MRJob):
    OUTPUT_PROTOCOL = TextProtocol

    def mapper(self, _, line):

        key = "key"
        # 去掉url地址
        line = re.split("\t", line)[1]
        # 替换特殊字符
        line = line.replace(" —", "")
        # 替换一些标点符号
        line = re.sub("[,.;()«»-]", "", line)
        # 按空格分隔
        words = re.split(r"\s", line)

        # 循环
        for word in words:
            # 过滤为空的字符
            if word != '':
                out = word + "|" + str(len(word))
                yield key, out

    def reducer(self, _, lines):
        max_cnt = 0
        max_word = None
        for line in lines:
            word, cnt = line.split('|')
            cnt = int(cnt)
            if cnt > max_cnt:
                max_cnt = cnt
                max_word = word

        yield str(max_word), str(max_cnt)


if __name__ == '__main__':
    langgest_word.run()
