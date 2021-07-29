from reglang import fa

#-----------------------#
delta_n8 = {  # DFA Martin, 4th Ed., p.76 (for minimization algo)
    (0, 'a') : 1,
    (0, 'b') : 9,
    (1, 'a') : 8,
    (1, 'b') : 2,
    (2, 'a') : 3,
    (2, 'b') : 2,
    (3, 'a') : 2,
    (3, 'b') : 4,
    (4, 'a') : 5,
    (4, 'b') : 8,
    (5, 'a') : 4,
    (5, 'b') : 5,
    (6, 'a') : 7,
    (6, 'b') : 5,
    (7, 'a') : 6,
    (7, 'b') : 5,
    (8, 'a') : 1,
    (8, 'b') : 3,
    (9, 'a') : 7,
    (9, 'b') : 8
}
n8 = fa.dfa(delta=delta_n8, start=0, finals={3, 4, 8, 9})
print('\nDFA n8:')
print(40*'-')
print(n8)
print(40*'-')
print('\nAbout to minimize n8 (method 1: L&P)')
min1_n8 = n8.minimized1(verbose=True)
print('\nMinimized n8: (method 1: L&P)')
print(40*'-')
print(min1_n8)
print(40*'-')
print('\nAbout to Minimize n8 (method 2: marking algo)')
min2_n8 = n8.minimized2(verbose=True)
print('\nMinimized n8: (method 2: marking algo)')
print(40*'-')
print(min2_n8)
print(40*'-')
#-----------------------#
print(f'min1_n8.equiv(min2_n8) is {min1_n8.equiv(min2_n8)}')
