n = int(input())

l = [0 for i in range(n)]
l[1] = 1

for i in range(2,n):
    l[i] = l[i-1] + l[i-2]

d = l[n-1]%10
print(d)