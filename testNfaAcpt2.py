import fa

delta_m3 = {   # NFA fig 2.9 p.70 L&P, language: (aa* U aa*b U b)(ep U (aUb)a*)
    (0, 'b'):{2},
    (0, '') :{1},
    (1, 'a'):{0, 4},
    (1, '') :{2, 3},
    (2, 'b'):{4},
    (3, 'a'):{4},
    (4, '') :{3}
}
m3 = fa.nfa(delta=delta_m3, start=0, finals={4})
print()
print('NFA m3 is as follows:')
print(m3)
print()
for inpstr in ['', 'a', 'b', 'aab', 'aaba', 'aabba', 'aabbb', 'aabbabab']:
    print('[accept version 1]')
    print(f'NFA m3 {"accepts" if m3.accept1(inpstr) else "does not accept"} "{inpstr}"')
    print('[accept version 2]')
    print(f'NFA m3 {"accepts" if m3.accept(inpstr) else "does not accept"} "{inpstr}"')
    print()
