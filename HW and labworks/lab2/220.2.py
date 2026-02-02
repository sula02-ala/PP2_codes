n = int(input())

doc = {}
result=[]

for i in range(n):
    command = input().split()

    if command[0] == "set":
        doc[command[1]] = command[2]

    else: # вместо elif command[0]=="get"
        if command[1] in doc:
            result.append(doc[command[1]])
        else:
            result.append(f"KE: no key {command[1]} found in the document")

print("\n".join(result))