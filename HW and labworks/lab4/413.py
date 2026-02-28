import json

data = json.loads(input())
q = int(input())

for _ in range(q):
    query = input()
    current = data
    found = True
    

    parts = []
    temp = ""
    i = 0
    
    while i < len(query):
        if query[i] == '.':
            if temp:
                parts.append(temp)
                temp = ""
            i += 1
        
        elif query[i] == '[':
            if temp:
                parts.append(temp)
                temp = ""
            i += 1
            index = ""
            while query[i] != ']':
                index += query[i]
                i += 1
            parts.append(index)
            i += 1
        
        else:
            temp += query[i]
            i += 1
    
    if temp:
        parts.append(temp)


    for part in parts:
        try:
            if part.isdigit():
                current = current[int(part)]
            else:
                current = current[part]
        except:
            found = False
            break

    if found:
        print(json.dumps(current, separators=(',', ':')))
    else:
        print("NOT_FOUND")