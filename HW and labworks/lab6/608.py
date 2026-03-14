n = int(input())
numbers = list(map(int, input().split()))

unique = sorted(set(numbers))

print(*unique)