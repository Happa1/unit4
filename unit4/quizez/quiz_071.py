import random
n =int(input("enter the number"))
dict={10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
macaddress_list=[]
macaddress=''
count=0
for j in range(n):
    for i in range(12):
        rand=random.randrange(16)
        if rand > 9:
            letter=dict[rand]
        else:
            letter=str(rand)
        macaddress+=str(letter)

        count+=1
        if count==2:
            macaddress+=':'
            count=0
        macaddress_list.append(macaddress)
        macaddress=''

print(macaddress_list)
