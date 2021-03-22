#mohammad haje forosh

#Conver base 2 number to base 10 number!

Number = int(input("Enter a Binary number:"))

dec_value = 0

base = 1

temp = Number

while temp:
    last_digit = temp % 10 #ragham akhar bedast miyad
    temp = int(temp / 10)
    dec_value += last_digit * base
    base = base * 2
print("Decimal number of",Number,"is : ",dec_value)


