from compiler.scanner.scanner import Scanner
from compiler.tools import regular_expressions as RE
from compiler.scanner.transition_table import TransitionTable

s = Scanner()
t = TransitionTable()
t.build_table()
