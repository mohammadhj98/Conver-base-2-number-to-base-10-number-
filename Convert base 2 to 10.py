#mohammad haje forosh

#Conver base 2 number to base 10 number!
#---------------------------------
# binary_string=input("Enter a number :")
# x=(int(binary_string,2))
# print(x)

#----------------------------------------
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

#---------------------------------------------

# B=input("Enter a binary String: ")
# N=0
# L=len(B)
# sign=1
# while(sign):
#     for i in range(L):
#         x=int(B[i])
#         if x<0 or x>1:
#             B=input("Enter a correct Binary String: ")
#             L=len(B)
#             break
#         else:
#             sign=0
## for i in range(L):
#     x=int(B[i])
#     N=N+(x*pow(2,L-i-1))
# print("Number in Base 10 is: %d"%N)








#Number = input("Enter a number")   
#s = int(Number, 2)   
#print("Binary",Number,"is:",s) 

##################

