arr = []
print("Enter Number ")
n = int(input())
for i in range(1,n+1):
    print("Enter delay for user "+ str(i) )
    x = int(input())
    arr.append(x)

print("")
print("Cycle 1")
print("")

j = 1
start = 0
end = 417
for i in range(n):
    if(arr[i]<10):
        print("Slot "+ str(j) +" is assigned for user " + str(i + 1) +" : from "+str(start) +" to " +str(end))
        start = start + 417 + 1
        end = end + 417 + 1
        j +=1
    else :
        print("Slot is not assigned for user " + str(i + 1))
        
print("")
print("Cycle 2")
print("")
k=1

for i in range(n):
    if(arr[i]<10):
        print("Slot "+ str(k) +" is assigned for user " + str(i + 1) +" : from "+str(start) +" to " +str(end) + "   => IDLE")
        start = start + 417 + 1
        end = end + 417 + 1
        k +=1
    else :
        print("Slot "+ str(k) +" is assigned for user " + str(i + 1) +" : from "+str(start) +" to " +str(end))
        start = start + 417 + 1
        end = end + 417 + 1
        k +=1