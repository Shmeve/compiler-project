from compiler.scanner.scanner import Scanner
from compiler.tools import regular_expressions as RE

x = RE.l_e("a")
y = RE.l_e("e")

print(x)
print(type(x))
print(y)
print(type(y))

s = Scanner()
