#basic calculator!!!
v= int(input("enter no. 1 : "))
j= int(input("enter no. 2 : "))
k= input("enter operator  : ")
if k == "+" :
    print(f"addition is {v+j}")
elif k == "-" :
    print(f"subtraction is {v-j}")
elif k == "*" :
    print(f"multiplication is {v*j}")
elif k == "/" :
    print(f"division is {v/j}")
elif k == "%" :
    print(f"modulos is {v%j}")
else :
    print("enter valid operator!!")