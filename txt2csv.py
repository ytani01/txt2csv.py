#!/usr/bin/env python3
import sys


def getline():
    return sys.stdin.readline().strip()


while True:
    num = getline()
    if num == '':
        break
    eng = getline()
    jp = getline()
    dummy = getline()

    if num[0] in '0123456789':
        print("%s,%s,%s" % (num, eng, jp))
