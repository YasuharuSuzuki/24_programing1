s_1, s_2 = input().split()

if 'AB' != s_1:
    s_1 += 'O'

if 'AB' != s_2:
    s_2 += 'O'

s_all = s_1 + s_2
child_genotypes = []

if (('A' in s_1) and ('B' in s_2)) or (('B' in s_1) and ('A' in s_2)):
    child_genotypes.append('AB')

if 'A' in s_all:
    child_genotypes.append('A')

if 'B' in s_all:
    child_genotypes.append('B')

if ('O' in s_1) and ('O' in s_2):  # O型は劣勢遺伝のため、2つ以上ないと子どもが生まれない
    child_genotypes.append('O')

# 結果を出力
print(' '.join(child_genotypes))