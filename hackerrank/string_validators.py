# In the first line, print True if  has any alphanumeric characters. Otherwise, print False.
# In the second line, print True if  has any alphabetical characters. Otherwise, print False.
# In the third line, print True if  has any digits. Otherwise, print False.
# In the fourth line, print True if  has any lowercase characters. Otherwise, print False.
# In the fifth line, print True if  has any uppercase characters. Otherwise, print False.

# input >>> qA2

# output
#       True
#       True
#       True
#       True
#       True

if __name__ == '__main__':
    s = input()
    s_new = list(s)

    for a in s_new:
        if a.isalnum():
            print(True)
            break
    else:
        print(False)

    for b in s_new:
        if b.isalpha():
            print(True)
            break
    else:
        print(False)

    for c in s_new:
        if c.isdigit():
            print(True)
            break
    else:
        print(False)

    for d in s_new:
        if d.islower():
            print(True)
            break
    else:
        print(False)

    for e in s_new:
        if e.isupper():
            print(True)
            break
    else:
        print(False)

    