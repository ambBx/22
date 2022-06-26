a = input("введите а : ")
b = input("введите б : ")
a=str(a.lower())
b=str(b.lower())
if (a == 'и') or (a == '1') or (a=='true'):
    a = True
elif (a == 'л') or (a == '0') or (a=='false'):
    a = False
else:
    print("Ошибка ввода А")
print(a)
if (b == 'и') or (b == '1') or (b=='true'):
    b = True
elif (b == 'л') or (b == '0') or (b=='false'):
    b = False
else:
    print("Ошибка ввода B")
print(b)
print("A \t B \t AvB \t A&B \t не A \t не B")
print(a,"\t",b,"\t",(a or b),"\t",(a and b),"\t",(not a),"\t",(not b)) 

