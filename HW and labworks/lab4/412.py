import json

def deep_diff(a, b, path=""):
    diffs = []

    keys = set(a.keys()) | set(b.keys())

    for key in keys:
        new_path = f"{path}.{key}" if path else key

        if key not in a:
            diffs.append((new_path, "<missing>", b[key]))

        elif key not in b:
            diffs.append((new_path, a[key], "<missing>"))

        else:
            if isinstance(a[key], dict) and isinstance(b[key], dict):
                diffs.extend(deep_diff(a[key], b[key], new_path))
            elif a[key] != b[key]:
                diffs.append((new_path, a[key], b[key]))

    return diffs

A = json.loads(input())
B = json.loads(input())

differences = deep_diff(A, B)

if not differences:
    print("No differences")
else:
    differences.sort(key=lambda x: x[0])

    for path, old, new in differences:
        if old != "<missing>":
            old = json.dumps(old, separators=(',', ':'))
        if new != "<missing>":
            new = json.dumps(new, separators=(',', ':'))

        print(f"{path} : {old} -> {new}")