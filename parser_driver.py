import sys
from compiler.scanner.scanner import Scanner
from compiler.parser.parser import Parser

DEBUG_TEST_FILE = "final_demo_samples/sample_3"

args_len: int = len(sys.argv)

if args_len >= 2:
    s = Scanner(sys.argv[1])
else:
    s = Scanner(DEBUG_TEST_FILE)

token_sequence: list = s.scan_file()

print("----------\nScanner\n----------")
if args_len >= 3:
    s.log(sys.argv[2])
else:
    s.log()

print("----------\nParser\n----------")
p: Parser = Parser(token_sequence)
result: bool = p.parse()

if args_len >= 3:
    p.log_results(sys.argv[2])
    print('----------\nParsed: ' + str(result))
    print('----------\n')
else:
    p.log_results()
    print('----------\nParsed: ' + str(result))
    print('----------\n')

