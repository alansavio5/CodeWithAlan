# input >>> a
# output >>> 16 (ascii of 'a' is 97, so 9+7 = 16)

char = input("Enter a letter: ")
b = []
a = []

for i in char:
    ascii_value = ord(i)
    b.append(ascii_value)

    digit_sum = 0
    while ascii_value > 0:
        digit = ascii_value % 10
        digit_sum += digit
        ascii_value = ascii_value // 10
        a.append(digit_sum)

for j in range(0,len(a)):  
    print(chr(a[j]),end="")
