﻿# -*- coding: utf-8 -*-
"""
Utility functions, like date conversion and digit conversion
"""

__all__ = [
    "arabic_digit_to_thai_digit",
    "bahttext",
    "collate",
    "delete_tone",
    "digit_to_text",
    "eng_to_thai",
    "find_keyword",
    "countthai",
    "is_native_thai",
    "isthai",
    "isthaichar",
    "normalize",
    "now_reign_year",
    "num_to_thaiword",
    "rank",
    "reign_year_to_ad",
    "text_to_arabic_digit",
    "text_to_thai_digit",
    "thai_strftime",
    "thai_to_eng",
    "thai_digit_to_arabic_digit",
    "thaiword_to_num",
    "thai_time",
]


from .collate import collate
from .date import now_reign_year, reign_year_to_ad, thai_strftime
from .digitconv import (
    arabic_digit_to_thai_digit,
    digit_to_text,
    text_to_arabic_digit,
    text_to_thai_digit,
    thai_digit_to_arabic_digit,
)
from .keyboard import eng_to_thai, thai_to_eng
from .keywords import find_keyword, rank
from .normalize import delete_tone, normalize
from .numtoword import bahttext, num_to_thaiword
from .thai import countthai, isthai, isthaichar
from .thaiwordcheck import is_native_thai
from .wordtonum import thaiword_to_num
from .thai_time import thai_time
