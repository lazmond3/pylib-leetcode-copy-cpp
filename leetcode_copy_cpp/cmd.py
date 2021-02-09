# -*- coding: utf-8 -*-
import sys
import re

def main() :
    fname = sys.argv[1]

    with open(fname) as f:
        for line in f.readlines():
            line = line.rstrip()
            m = re.match(r"#include.*\"(mylib/.*.hpp)\"", line)
            if m:
                h_name = m.group(1)
                print("// " + line)
                with open(h_name) as f2:
                    for mine in f2.readlines():
                        mine = mine.rstrip()
                        print(mine)
            else:
                print(line)

