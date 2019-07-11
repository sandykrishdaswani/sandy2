sant1=input()
san2=''
san3='0ABCDEFGHIJKLMNOPQRSTUVWXYZABC'
for i in sant1:
    if i in san3:
        san4=san3.index(i)
        san4=san4+3
        san2=san2+san3[san4]
print(san2)
