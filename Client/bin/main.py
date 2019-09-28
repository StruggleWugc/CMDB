#!/usr/bin/env python

import os
import sys

BASE_DIR = os.path.dirname(os.getwcd())

# 设置工作目录，使得包和模块能够正常导入
sys.path.append(BASE_DIR)

from Client.core import handler

if __name__ == '__mian__':
    handler.ArgvHandler(sys.argv)
