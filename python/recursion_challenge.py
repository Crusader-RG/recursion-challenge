def factorial(x):
	if x == 1:
		return x
	return x * factorial(x - 1)
		

def palindrome(string):
	if len(string) < 1:
		return True
	if string[0] == string[-1]:
		return palindrome(string[1:-1])
	else:
		return False

def bottles(num):
	if num == 1:
		print(f"1 bottle\nno bottles")
		return
	print(f"{num} bottles")
	return bottles(num - 1)

def roman_num(num):
	roman = {
        "M": 1000,
        "CM": 900,
        "D": 500,
        "CD": 400,
        "C": 100,
        "XC": 90,
        "L": 50,
        "XL": 40,
        "X": 10,
        "IX": 9,
        "V": 5,
        "IV": 4,
        "I": 1 
     }
	
	if num == 0:
		return ""
	for key in roman.keys():
		if roman[key] <= num:
			return f"{key}" + f"{roman_num(num - roman[key])}"
		

