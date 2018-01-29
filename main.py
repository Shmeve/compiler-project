from compiler.scanner.scanner import Scanner
from compiler.tools import regular_expressions as RE
from compiler.scanner.transition_table import TransitionTable

s = Scanner("compiler/samples/sample_2")
s.scan_file()
s.log()
