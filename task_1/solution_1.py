a=input("enter a number: ")
b=-1                          #b=cамое большое число
for i in a:
	if int(i)>b:                #если символ больше принятого сейчас СБЧ, то о становится СБЧ
		b=int(i)

print(b)
