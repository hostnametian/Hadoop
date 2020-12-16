# -*- coding: UTF-8 -*-
import sys

cur_word = None
max_cnt = 0
max_word = None
for line in sys.stdin:
    key, value = line.strip().split('\t')
    # print value

    word, scnt = value.split('|')
    cnt = int(scnt)

    if cnt > max_cnt:
        max_cnt = cnt
        max_word = word

print('%s\t%s' % (max_word, max_cnt))
