#SMIT/19/PY/B2/08727 PY08727 SUMAIR AIJAZ aliasadzaidi123@gmail.com

dict={"name":"sumair","age":20,"address":"Hyderabad",117:"rollno"}
key=input("enter any key to find: ")

for i in dict.keys():
    if key == str(i):
        print("key exists")
        break
else:
    print("key does not exists")