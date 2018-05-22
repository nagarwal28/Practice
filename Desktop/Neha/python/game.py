def getA():
    print "Enter fame, fortune and secrets value for A"
    A = []
    for x in range(0,3):
        f=raw_input("Enter value")
        A.append(f)
    return A
def getB():
    print "Enter fame, fortune and secrets value for B"
    B = []
    for x in range(0,3):
        ff=raw_input("Enter value")
        B.append(ff)
    return B
def getC():
    print "Enter fame, fortune and secrets value for C"
    C = []
    for x in range(0,3):
        fff=raw_input("Enter value")
        C.append(fff)
    return C
def findmin(P):
    min=P[0]
    if(P[1]<min):
        min=P[1]
    elif(P[2]<min):
        min=P[2] 
    return min
def findmax(P):
    max=P[0]
    i=0
    if(P[1]>max):
        max=P[1]
        i=1
    elif(P[2]>max):
        max=P[2] 
        i=2
    return i

def main():
  print("Hello World!")
  A=getA()
  B=getB()
  C=getC()
  minofa=findmin(A)
  minofb=findmin(B)
  minofc=findmin(C)
  print minofa
  print minofb
  print minofc
  Min =[minofa, minofb, minofc]
  maxindex=findmax(Min)
  print "Index is ", maxindex
if __name__== "__main__":
  main()
