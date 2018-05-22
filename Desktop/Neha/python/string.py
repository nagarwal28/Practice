str = raw_input("Enter a string")
print str
str = str.replace(' ','')
str = str.lower()
sum=0
length=len(str)
print str
print length
for x in range(0,length):
    seq=0
    seq=ord(str[x])-96
    sum=sum+seq
print sum
while(sum>9):
    dig=sum%10    
    quo=sum/10
    sum=dig+quo
print sum




