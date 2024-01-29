#Um inteiro N representando a quantidade de pedaços. (0 < N < 200)
#N linhas contendo um inteiro M e um caractere C. (1 < M <= N)
n = int(input())

words = {}

for i in range(n):
    key, value = input().split()
    words[int(key)] = value

sorted_words = dict(sorted(words.items()))
for value in sorted_words.values():
    print(value,end="")
