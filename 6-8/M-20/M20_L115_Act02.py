def match_words(words):
	ctr = 0
	Lst = [] # empty list

	for w in words:
		if len(w) > 1 and w[0] == w[-1]:
			ctr = ctr + 1
			Lst.append(w) # adding the element in the Lst
	
	print("List of words with first and last character same")
	print(Lst)
	return ctr

word_list = ['abc', 'cfc','xyz', 'aba', '1221']
count = match_words(word_list)
print("Number of words having first and last character same:", count)