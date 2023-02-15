url = input("Enter the url:")
x = url.split("/")

if(x[0]=="https:" or x[0]=="http:"):
    x=x[2].split(".")
else:
    x=x[0].split(".")
    
domain = ""
if(len(x)==2):
    domain = x[0]+"."+x[1]
else:
    domain = x[1]+"."+x[2]

print("The Domain Name is: ", domain)