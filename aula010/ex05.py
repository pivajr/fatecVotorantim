L1 = [10, 12, 13, 14, 15, 18, 20]
L2 = [10, 12, 14, 18, 21]
for k in range(-1, -len(L1), -1):
    if L1[k] in L2[-5:-2]:
        print L1[k]