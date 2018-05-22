str=raw_input("Enter a string")
for x in range (0,len(str)):
    if ord(str[x])>64 and ord(str[x])<91:
        print '\n'
    print str[x]

