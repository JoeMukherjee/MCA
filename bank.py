import emi as emi
print("Enter The total amount of the money you want as a loan")
p=float(input())
print("Enter the percentage of the interest you are offered from the bank")
r=float(input())
print("Enter the number of years you will be taking to clear the debt")
t=int(input())
print("From this month onwards you will be paying " + str(round(emi.emi(p,r,t),2))+ " Rs. every month till the end of the comming " + str(t)+ " years")
