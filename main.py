import sys
from compiler.scanner.scanner import Scanner
from compiler.parser.parser import Parser
from compiler.semantic_analysis.semantic_analyzer import SemanticAnalyzer

DEBUG_TEST_FILE = "compiler/samples/sample_4"

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
    print('----------\n'+str(result))
else:
    p.log_results()
    print('----------\nResult: ' + str(result))

print("----------\nSemantic Analysis\n----------")
sa: SemanticAnalyzer = SemanticAnalyzer(p.ast_root)
sa.analyze()

if args_len >= 3:
    sa.log_results(sys.argv[2], sa.global_table)
else:
    sa.log_results(root_node=sa.global_table)
