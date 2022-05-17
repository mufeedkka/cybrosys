list=[]
evenlist=[]
for i in range(0,2001):
    # print(i)
    list.append(i)
print("list is\n")
print(list)
for i in list:
    if i % 2==0:
        evenlist.append(i)
print("even list is\n")
print(evenlist)
d=dict()
for i in range(0,1001):
    d[i]=i*2
print("dictionary is \n")
print(d)