s1 = input ("Enter a sentence : ")
s2 = input ("Enter the word to find its occurance : ")
words = s1.split()
count = 0
for i in words:
	if i == s2 :
		count += 1
print(f"The number of occurance of {s2} in the sentence is : {count}")
