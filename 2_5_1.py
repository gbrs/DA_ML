'''
Парадокс Монти Холла.
Шафлил список из коз и авто.
Полагал, что всегда выбирают левую дверь.
Это не противоречит ничему, вроде. Можно представить, что мы выбрали дверь
и все двери левее (с объектами) переместили в конец.
'''

import random

N = 100000
cnt_persistent = cnt_variable = 0
for _ in range(N):
    lst = ['к', 'к', 'а']
    random.shuffle(lst)
    if lst[0] == 'а':
        cnt_persistent += 1
    else:
        cnt_variable += 1
if input() == 'No':
    print(round(cnt_persistent / N, 2))
else:
    print(round(cnt_variable / N, 2))
