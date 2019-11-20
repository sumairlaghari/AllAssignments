#SMIT/19/PY/B2/08727 PY08727 SUMAIR AIJAZ aliasadzaidi123@gmail.com

list=[10,20,30,20,20,30,40,50,-20,60,60,-20,-20]
list2=[]

for i in range(0,13):
    for j in range(0,13):
        if list[i]==list[j] and i!=j and list[i] not in list2:
            list2.append(list[i])

print(list2)
