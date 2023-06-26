import string
dictionary = {letter: 0 for letter in string.ascii_uppercase}

a = str(input())
for i in a.upper():
	dictionary[i] += 1
def get_key_with_max_value(dictionary):
	max_value = max(dictionary.values())
	keys_with_max_value = [key for key, value in dictionary.items() if value == max_value]
	return keys_with_max_value

keys = get_key_with_max_value(dictionary)
if len(keys) == 1:
	print(keys[0])
else :
	print("?")