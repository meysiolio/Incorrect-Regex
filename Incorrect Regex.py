import re

T = int(input())
result = []

for i in range(T):
    try:
        re.compile(input())
        result.append(True)
    except:
        result.append(False)

for j in result:
    print(j)