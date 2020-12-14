# -*- coding: UTF-8 -*-

from mrjob.job import MRJob
from mrjob.protocol import TextProtocol
from mrjob.step import MRStep
import re


class upper_words_ten(MRJob):
    OUTPUT_PROTOCOL = TextProtocol

    def mapper(self, _, line):
        # 去掉url
        line = re.split("\t", line)[1]
        # 替换特殊字符
        line = line.replace(" —", "")
        # 替换一些标点符号
        line = re.sub("[,.;()«»-]", "", line)
        # 按空格分隔
        words = re.split(r"\s", line)
        for word in words:
            if word[0].isupper():
                yield (word, 1)

    def combiner(self, word, counts):
        yield (word, sum(counts))

    def reducer(self, word, counts):
        word_sum = sum(counts)
        if word_sum > 10:
            yield word, str(word_sum)


# never forget
if __name__ == '__main__':
    upper_words_ten.run()
