import random 

def shuffle(string):
	tempList = list(string)
	random.shuffle(tempList)
	return ''.join(tempList)

#Add 2 upper case characters
uppercaseLetter1= chr(random.randint(65,90))
uppercaseLetter2= chr(random.randint(65,90))

#Add 2 Lower case characters
lowercaseLetter1= chr(random.randint(97,122))
lowercaseLetter2= chr(random.randint(97,122))

#Add 2 special characters
speicalLetter1= chr(random.randint(33,47))
specialLetter2= chr(random.randint(33,47))

#Add 2 Numbers
number1= chr(random.randint(48,57))
number2= chr(random.randint(48,57))


password = uppercaseLetter1 + uppercaseLetter2 + lowercaseLetter1 + lowercaseLetter2 + speicalLetter1 + specialLetter2 + number1 + number2 

#randomize
password = shuffle(password)

#Ouput
print(password)