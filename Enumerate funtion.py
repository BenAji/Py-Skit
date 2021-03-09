def skip_elements(elements):
	# code goes here
	i=0
	x=[]
	for element in (elements):
		while i < len(elements):
			#elements[i]
			x.append(elements[i])
			i=i+2
			
	for index, y in enumerate(x):
		if (int(index+1))%2 != 0:
			print (" {} ".format(y) +" is in an odd position" )
		else :
			print(" {} ".format(y) +" is in an even position")

	return (x)   

#print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
#print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']