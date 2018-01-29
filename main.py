import sys
from compiler.scanner.scanner import Scanner

args_len: int = len(sys.argv)

if args_len >= 2:
    s = Scanner(sys.argv[1])
else:
    s = Scanner()

s.scan_file()

if args_len >= 3:
    s.log(sys.argv[2])
else:
    s.log()
