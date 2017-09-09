# -*- coding: utf-8 -*-
import unicodedata


class StringUtils:
    @classmethod
    def is_japanese(cls, str):
        for char in str:
            lang = unicodedata.name(char)
            if lang.find("CJK UNIFIED | HIRAGANA | KATAKANA"):
                return True
        return False
