# -*- coding: UTF-8 -*-

from mrjob.job import MRJob
from mrjob.protocol import TextProtocol
from mrjob.step import MRStep
import re
"""
Напишите программу, чтобы найти слово, которое встречается чаще всего.
"""


class Most_frequently_word(MRJob):
    OUTPUT_PROTOCOL = TextProtocol

    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_words,
                   combiner=self.combiner_count_words,
                   reducer=self.reducer_count_words),
            MRStep(reducer=self.reducer_find_max_word)
        ]

    def mapper_get_words(self, _, line):
        # 去掉url地址
        line = re.split("\t", line)[1]
        # 替换特殊字符
        line = line.replace(" —", "")
        # 替换一些标点符号
        line = re.sub("[,.;()«»-]", "", line)
        # 按空格分隔
        words = re.split(r"\s", line)
        for word in words:
            yield (word.lower(), 1)

    def combiner_count_words(self, word, counts):
        yield (word, sum(counts))

    def reducer_count_words(self, word, counts):
        yield None, (word + "|" + str(sum(counts)))

    def reducer_find_max_word(self, _, word_counts):
        max_word = None
        max_count = 0
        for word_count in word_counts:
            word, count = word_count.split("|")
            if int(count) > max_count:
                max_count = int(count)
                max_word = word

        yield max_word, str(max_count)


if __name__ == '__main__':
    Most_frequently_word.run()
