lst = [i for i in input().split(' ')]
query=input()
ans=[]
for i in lst:
    if i[:len(query)]==query:
        ans.append(i)
print(ans)
        
