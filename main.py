a= int(input("Enter a Starting a Range :"))
b= int(input("Enter a Ending   a Range 🏁:"))
for i in range(a,b):
    g=i
    s=str(i)
    l=len(s)
    counter = 0

    while i>0:
        z=i%10
        x=z**l
        counter=counter+x
        i=i//10
        if counter==g:
            print(counter,"- is a Armstrong number")
        else:
            continue
