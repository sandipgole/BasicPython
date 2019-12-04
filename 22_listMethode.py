list=[1,2,3,4,5,5]
#list.sort()
#list.reverse()
'''print(list.count(5))
list2=list.copy()'''
list2=[2,2,2,4,5,6,6,7]
qniquelist=[]
for number in list2:
    if number not in qniquelist:
        qniquelist.append(number)
print(qniquelist)
