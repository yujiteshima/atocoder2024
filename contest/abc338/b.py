S = input()
ary = [0] * 26
for s in S:
  ord_s = ord(s) - 97
  ary[ord_s] += 1
max_count = 0
max_idx = -1

for i, a in enumerate(ary):
  if max_count < a:
    max_count = a
    max_idx = i
print(chr(max_idx + 97))
