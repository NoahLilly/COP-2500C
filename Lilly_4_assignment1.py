p=int(input("what is the principal amount? "))
r=float(input("what is the rate? "))/100
t=int(input("what is the number of years? "))
n=int(input("what is the number of times the interest is compounded per year? "))
a=(p*((1+(r/n))**(n*t)))
a="{:.2f}".format(a)
print(a)
