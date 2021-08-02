from reglang.nfa import nfa

delta_m4 = { # NFA ex.2.2.6 (a): L = (ab U aab U aba)*
    (0, 'a'):{1},
    (1, 'a'):{2},
    (1, 'b'):{0, 3},
    (2, 'b'):{0},
    (3, 'a'):{0}
}
m4 = nfa(delta=delta_m4, start=0, finals={0})
print()
print('NFA m4 is as follows:')
print(m4)
print()
tlist = ['', 'a', 'b', 'ab', 'aab', 'aba', 'bab', 'abab','abaa', 'abaaababab', 'abaaabb']
for inpstr in tlist:
    print('[accept version 1]')
    print(f'NFA m4 {"accepts" if m4._accept0(inpstr) else "does not accept"} "{inpstr}"')
    print('[accept version 2]')
    print(f'NFA m4 {"accepts" if m4.accept(inpstr) else "does not accept"} "{inpstr}"')
    print()

