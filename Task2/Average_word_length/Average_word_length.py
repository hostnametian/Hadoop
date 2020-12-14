# -*- coding: UTF-8 -*-

from mrjob.job import MRJob
from mrjob.protocol import TextProtocol
import re


class Average_word_length(MRJob):
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
                yield key, len(word)

    def reducer(self, _, lens):
        # 单词总长度
        # s = sum(lens)
        # 单词数量
        num = 0
        s = 0
        for le in lens:
            num = num + 1
            s = s + le

        avg_len = s / num

        yield None, str(avg_len)


if __name__ == '__main__':
    Average_word_length.run()
