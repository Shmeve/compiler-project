import re


def l_e(string: str) -> bool:
    return bool(re.match('[a-df-gA-Z]', string))


def e(string: str) -> bool:
    return string == 'e'


def d_0(string: str) -> bool:
    return bool(re.match('[1-9]', string))


def zero(string: str) -> bool:
    return string == '0'

