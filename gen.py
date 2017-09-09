# -*- coding: utf-8 -*-

import os
import sys

from file.file_utils import FileUtils
from char.string_utils import StringUtils

LOG_DIR = "./log/"


def main():
    argv = sys.argv
    if len(argv) < 2: return
    _error_size = open(LOG_DIR + "size.log", "wt")
    _error_japanese = open(LOG_DIR + "japanese.log", "wt")
    for file in FileUtils.walk(sys.argv[1]):
        if FileUtils.check_extension(file, ".psd", ".png"): _error_size.write(
            "file: %s, size:%s" % (file, str(os.path.getsize(file))))
        if StringUtils.is_japanese(file): _error_japanese.write("file %s" % file)

    _error_size.close()
    _error_japanese.close()


if __name__ == '__main__':
    main()
