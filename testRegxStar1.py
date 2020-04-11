from fa import *

a = regx('a')
print(f"NFA for regular expression '{a.val}' is")
print(a.nfa)

astar = a.star()
print(f"NFA for regular expression 'a.star()' with value '{astar.val}' is")
print(astar.nfa)

for s in ['', 'a', 'aa', 'aaa', 'b', 'ab', 'aaa3']:
    print(f"regx {astar.val} : string '{s}' -> {astar > s}")
print()

