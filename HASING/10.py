n = [1,2,4,5,6,2,7,9,10,2,3,5]
m= [22,3,4,6,8,2,5,9,2,1]

hash_list=[0]*11

for i in range(0, len(n)):
    if (0<=n[i]<=10):
        hash_list[n[i]]+=1

for i in range(0, len(m)):
    if (0<=m[i]<=10):
        print(m[i], hash_list[m[i]]) 