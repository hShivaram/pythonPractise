votes = ["pasta", "pasta", "pasta", "pasta", "pasta", "paratha", "paratha", "paratha"]

d = {}

# print the list without duplicates
for item in votes:
    if item not in d:
        d[item] = 1
    else:
        d[item] += 1

m = max(d.values())
count = 0
for m in d.values():
    count += 1


for item in d.keys():
    if d[item] == m:
        print(item)
        break
    else:
        print("NOTA")
