a=input('enter your name - ')
b=int(input('enter your class - '))
c=float(input('enter subject 1 marks - '))
d=float(input('enter subject 2 marks - '))
e=float(input('enter subject 3 marks - '))
f=float(input('enter subject 4 marks - '))
g=float(input('enter subject 5 marks - '))
per=(c+d+e+f+g)/5
print("Name  : ",a)
print("Class  : ",b)
print("Percentage  : ",per)

if per > 60 :
    print("grade A")
elif per >= 50 :
    print("grade B")
elif per >=40 :
    print("grade C")
elif per >=33 :
    print("grade D")
else :
    print("Better Luck, Next time!")
