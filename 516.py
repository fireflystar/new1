li = range(1,10)

li_r = list()
li_temp = list()

i = 0
j = 0
k = 0

while i < len(li):
	li_temp.append(li[i])
	print li[i]
	
	j += 1
	if j == 2:
		print li_temp
		li_temp = list()
		j = 0

	i += 1
	
