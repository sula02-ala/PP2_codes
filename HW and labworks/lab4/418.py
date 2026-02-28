x1, y1 = list(map(float, input().split()))
x2, y2 = list(map(float, input().split()))

k = y2/y1
s = x2 - x1
l = s/(1 + k)
result = x1 + l
y = 0.0

print(f"{result:.10f} {y:.10f}")