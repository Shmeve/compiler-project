import re


def l_e(string: str) -> bool:
    return bool(re.match('[a-df-zA-Z]', string))


def e(string: str) -> bool:
    return string == 'e'


def d_0(string: str) -> bool:
    return bool(re.match('[1-9]', string))


def zero(string: str) -> bool:
    return string == '0'


def eol(string: str) -> bool:
    return string == '\n'


def eof(string: str) -> bool:
    return string == 'EOF'


def sp(string: str) -> bool:
    return string == ' '
