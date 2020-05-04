p=input("Enter the  Principal Amount in Taka: ")
p=int(p)
n=input("Enter the Time Period in years: ")
n=int(n)
r=input("Enter the rate of interest in %: ")
r=int(r)

si = (n*p*r)/100
print("The total interest in "+str(n)+" years is "+str(si)+" Taka")