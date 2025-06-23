# a=input('enter string one : ')
# b=input('enter string two : ')
a = " me Bhumi"
b = " Porwal "
cat=a+b
print(cat)
print(cat.upper())
print(cat.lower())
print(cat.title())
print(cat.replace("b", "v"))
print(cat.swapcase())
print(cat.casefold())
print(cat.find("m"))
print(cat.rfind("m"))
print(cat.count("m"))
print(cat.startswith("m"))
print(cat.endswith("l"))
print(cat.strip())
print(len(cat))

# Returns True/False
print("="*20)
i="rishu18"
j="BHUMI"
k="rishu"
l="   "
m="1234"
v="Taehyung"
n="1kite"
o="kite_1"
p= "hello!\nWelcome to my first python coding day\nbyee bye!!"
print(i.isalnum())
print(j.islower())
print(k.isupper())
print(l.isspace())
print(m.isdigit())
print(v.istitle())
print(m.isdecimal())
print(n.isidentifier())
print(o.isidentifier())
print(p.splitlines())
q= ['Aaloo', 'Bhalu', 'Chalu']
result= '-'.join(q)
print(result)
