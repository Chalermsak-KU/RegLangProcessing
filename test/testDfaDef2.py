from reglang.dfa import *
from reglang.nfa import *
from reglang.regx import *

delta = {   # a DFA that accepts the empty set
}
dfa1 = dfa(delta=delta, start='s', finals={'f'})
print('DFA that accepts the empty set is')
print(40*'-')
print(dfa1)
print(40*'-')

