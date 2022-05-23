# -*- coding: utf-8 -*-

# Author: 1dragosh

import random
import re


def spin(spintax, delimiter='|'):
    def _sel(m):
        ch = m.group(1).split(delimiter)
        return ch[random.randint(0, len(ch) - 1)]

    what = re.compile('{([^{}]*)}')
    while True:
        spintax, x = what.subn(_sel, spintax)
        if x == 0:
            break
    return spintax.strip()()


if __name__ == "__main__":
    print(spin("{ Hi! | Hello! | Hey! }"))
