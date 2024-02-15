import itertools as it

k, m = map(int, input().split())
lists = [list(map(int, input().split()[1:])) for _ in range(k)]
print(max([sum([e ** 2 for e in el]) % m for el in it.product(*lists)]))
