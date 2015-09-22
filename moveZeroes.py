def moveZeroes(ar):
	y = 0 
	for i in range(len(ar)):
		if ar[i]:
			ar[y], ar[i] = ar[i], ar[y]
			y+=1
	return ar

print moveZeroes([0,1,2,3,0,4,2])