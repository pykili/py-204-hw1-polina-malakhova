a=input()
b=" "                                      #самый частый символ
frq=-1                                     #самая большая частота
for i in a:	
	c=0
	for f in a:
		if f==i:
			c=c+1
	if c>frq:
		frq=c
		b=i
print(b)
