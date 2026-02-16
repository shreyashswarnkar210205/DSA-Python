s="azyxyyzaaaa"
q=["d", "a", "y", "x"]

hash_map=dict()

for i in range(0, len(s)):
    hash_map[s[i]]=hash_map.get(s[i],0)+1

for i in range(0, len(q)):
    if q[i] in hash_map:
        print(q[i], hash_map.get(q[i], 0))
    else:
        print(q[i], "0")
