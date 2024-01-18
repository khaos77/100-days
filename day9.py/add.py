n = int(input())
lis = []
for i in range(n):
    stamp = input()
    lis.append(stamp)

s = set(lis)
print(len(s))