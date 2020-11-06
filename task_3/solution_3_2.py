alphabet=""
alphabet1=str(alphabet)
for smth in 'a'*10:
	a=input()
	for i in a:
		if i not in alphabet:
			alphabet=alphabet + str(i)
			alphabet1=str(alphabet)
		else:
			alphabet1=str(alphabet)
print(alphabet1)
