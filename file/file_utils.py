# -*- coding: utf-8 -*-
import os


class FileUtils:
    @classmethod
    def walk(cls, directory):
        for root, dirs, files in os.walk(directory):
            yield root
            for file in files:
                yield os.path.join(root, file)

    @classmethod
    def check_extension(cls, file, *extension):
        name, ext = os.path.splitext(file)
        return extension.__contains__(ext)
