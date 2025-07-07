filename = input ("Enter the filename : ")
with open (filename, 'r') as file:
	text = file.read()
words = text.split()
word_dict = {}
for word in words:
	if word in word_dict :
		word_dict[word] = word_dict[word] + 1	
	else :
		word_dict[word] = 1
max_wrd = max (word_dict, key = word_dict.get)
print(f" The most frequently used word is {max_wrd} with a frequency of {word_dict[max_wrd]}")

