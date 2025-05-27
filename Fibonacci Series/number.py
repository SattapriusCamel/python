print("The Fibonnaci series")

n=int(input("Enter the times want to the number go into: "))
fn=0
sn=1
nextnum=sn
ronk=1

while nextnum<= n:
    print(ronk,end=" ")
    nextnum += 1
    fn, sn = sn, ronk
    ronk = fn + sn
print()