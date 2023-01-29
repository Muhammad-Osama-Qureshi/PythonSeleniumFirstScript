

fruits=["Apple","Orange","Banana"]
for fruit in fruits:
    print("We should eat {} everyday".format(fruit))

temp=40
while temp>32:
    print("Temperature is {}".format(temp))
    temp-=1
    if temp==35:
     break
for i in range(1,20):
    if i==15:
        print("We are skipping 15")
        continue
    print("The number is {}".format(i))