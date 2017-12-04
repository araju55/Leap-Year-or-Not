month = int(input("Enter the month"))
year = int(input("Enter the year"))

days31 = [1,3,5,7,8,10,12]
days30 = [4,6,9,11]

if month == 2:
                if year%4 == 0 and (year%100!=0 or year%400==0):
                                print("The month: ", month, "has 29 days")
                else:
                                print("The month: ", month, "has 28 days")
elif month in days31:
    print("The month: ",month, "Has 31 days")

elif month in days30:
    print("The month: ",month, "Has 30 days")

