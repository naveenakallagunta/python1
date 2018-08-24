i=raw_input()
if((i>='a' and i<='z')or(i>='A'and i<='z')):
	if i in('a','e','i','o','u','A','E','I','O','U'):
		print("Vowel")
	else:
		print("Consonant")
else:
 	print("Invalid")
