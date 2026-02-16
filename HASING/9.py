n = [1,2,4,5,6,2,7,9,10,2,3,5]
m= [22,3,4,6,8,2,5,9,2,1]

hash_map=dict()

for i in range (0, len(n)):
    hash_map[n[i]]=hash_map.get(n[i],0)+1

for i in range (0, len(m)):
    if m[i] in hash_map:
        print(m[i], hash_map.get(m[i],0))